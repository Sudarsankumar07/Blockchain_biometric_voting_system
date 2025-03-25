import cv2
import numpy as np
import os
import sqlite3
from datetime import datetime
from fingerprint_Matching import is_fingerprint_in_db  # Import the function

class VotingSystem:
    def __init__(self, db_name='voter_blockchain.db', fingerprint_db_folder="fingerprint_database"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.fingerprint_db_folder = fingerprint_db_folder
        # self.add_candidate_vote_column()

    def column_exists(self, table, column):
        """Check if a column exists in a table."""
        self.cursor.execute(f"PRAGMA table_info({table})")
        columns = [row[1] for row in self.cursor.fetchall()]  # Extract column names
        return column in columns
    
    def add_candidate_vote_column(self):
        """
        Optionally add a candidate_vote column to the users table if it doesn't exist.
        Run this once to modify your schema.
        """
        try:
            if not self.column_exists("voters", "candidate_vote"):
                self.cursor.execute("ALTER TABLE voters ADD COLUMN candidate_vote TEXT")
                self.conn.commit()
                print("Added column: candidate_vote")
            else:
                print("Column candidate_vote already exists.")

            if not self.column_exists("voters", "vote_timestamp"):
                self.cursor.execute("ALTER TABLE voters ADD COLUMN vote_timestamp DATETIME")
                self.conn.commit()
                print("Added column: vote_timestamp")
            else:
                print("Column vote_timestamp already exists.")

        except sqlite3.OperationalError as e:
            print("Error adding column:", e)

    def voter_verify(self, name, age, fingerprint_img_path):
        """
        Verify that the voter exists in the database and check fingerprint.
        """
        # Use deep learning-based fingerprint verification
        match_found, matched_file = is_fingerprint_in_db(fingerprint_img_path, self.fingerprint_db_folder)

        if not match_found:
            print("Fingerprint verification failed! You are not registered.")
            return False

        # If fingerprint is found, verify voter's details in the database
        query = '''
            SELECT * FROM voters 
            WHERE name = ? AND age = ? AND is_verified = 0
        '''
        self.cursor.execute(query, (name, age))
        result = self.cursor.fetchone()

        return result is not None

    def vote(self, name, age, fingerprint_img_path):
        """
        Verify voter credentials, allow voting for candidate A or B,
        record the vote, and update the voter's status.
        """
        if not self.voter_verify(name, age, fingerprint_img_path):
            print("Voting failed: You are either not in the database or have already voted.")
            return

        vote = input("Vote for candidate A or B: ").strip().upper()
        if vote not in ['A', 'B']:
            print("Invalid vote. Please choose candidate A or B.")
            return

        # Record the vote
        update_query = '''
            UPDATE voters
            SET candidate_vote = ?, is_verified = 1,
                vote_timestamp = ?
            WHERE name = ? AND age = ? AND is_verified = 0
        '''
        self.cursor.execute(update_query, (vote, datetime.now().isoformat(), name, age))
        self.conn.commit()
        print("Vote recorded successfully.")

    def result(self):
        """
        Count votes for candidate A and candidate B and display the winner.
        """
        self.cursor.execute('SELECT COUNT(*) FROM voters WHERE candidate_vote = "A"')
        count_A = self.cursor.fetchone()[0]
        
        self.cursor.execute('SELECT COUNT(*) FROM voters WHERE candidate_vote = "B"')
        count_B = self.cursor.fetchone()[0]
        
        print("\n--- Voting Results ---")
        print(f"Candidate A: {count_A} votes")
        print(f"Candidate B: {count_B} votes")
        
        if count_A > count_B:
            print("Candidate A wins")
        elif count_B > count_A:
            print("Candidate B wins")
        else:
            print("It's a tie!")

    def close_connection(self):
        self.conn.close()

if __name__ == "__main__":
    # Get voter details
    name = input("Enter your name: ").strip()
    try:
        age = int(input("Enter your age: ").strip())
    except ValueError:
        print("Invalid age. Please enter a number.")
        exit()

    fingerprint_img_path = input("Enter the path to your fingerprint image: ").strip()

    voting_system = VotingSystem()
    voting_system.vote(name, age, fingerprint_img_path)
    # voting_system.result()
    # voting_system.close_connection()
