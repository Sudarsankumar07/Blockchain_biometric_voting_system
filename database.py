import sqlite3
import hashlib
import uuid
import datetime

class VoterBlockchainDatabase:
    def __init__(self, db_name='voter_blockchain.db'):
        """Initialize the database connection"""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Create voters table with blockchain-like attributes"""
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS voters (
            voter_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            address TEXT,
            fingerprint_hash TEXT UNIQUE NOT NULL,
            blockchain_hash TEXT,
            registration_timestamp DATETIME,
            is_verified BOOLEAN DEFAULT 0
        )
        ''')
        self.conn.commit()

    def generate_blockchain_hash(self, voter_data):
        """
        Generate a blockchain-style hash for voter data
        Combines voter details with a timestamp for uniqueness
        """
        # Combine voter data into a single string
        data_string = f"{voter_data['name']}{voter_data['fingerprint_hash']}{datetime.datetime.now()}"
        
        # Create a SHA-256 hash
        return hashlib.sha256(data_string.encode()).hexdigest()

    def register_voter(self, name, age, address, fingerprint):
        """
        Register a new voter with blockchain-style verification
        """
        # Generate unique voter ID
        voter_id = str(uuid.uuid4())
        
        # Hash the fingerprint
        fingerprint_hash = hashlib.sha256(fingerprint.encode()).hexdigest()
        
        # Prepare voter data dictionary
        voter_data = {
            'voter_id': voter_id,
            'name': name,
            'fingerprint_hash': fingerprint_hash
        }
        
        # Generate blockchain hash
        blockchain_hash = self.generate_blockchain_hash(voter_data)
        
        try:
            # Insert voter into database
            self.cursor.execute('''
            INSERT INTO voters 
            (voter_id, name, age, address, fingerprint_hash, blockchain_hash, registration_timestamp) 
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                voter_id, 
                name, 
                age,
                address,
                fingerprint_hash, 
                blockchain_hash, 
                datetime.datetime.now()
            ))
            
            self.conn.commit()
            return {
                'voter_id': voter_id,
                'blockchain_hash': blockchain_hash
            }
        except sqlite3.IntegrityError:
            print(f"Voter {name} already exists or fingerprint already registered")
            return None

    def insert_sample_voters(self):
        """
        Insert five sample voters with diverse backgrounds
        """
        sample_voters = [
            {
                'name': 'John Smith',
                'age': 35,
                'address': '123 Main St, Cityville, ST 12345',
                'fingerprint': 'john_unique_fingerprint_001'
            },
            {
                'name': 'Emily Rodriguez',
                'age': 28,
                'address': '456 Oak Avenue, Townsburg, ST 67890',
                'fingerprint': 'emily_unique_fingerprint_002'
            },
            {
                'name': 'Michael Chang',
                'age': 42,
                'address': '789 Pine Road, Villagetown, ST 54321',
                'fingerprint': 'michael_unique_fingerprint_003'
            },
            {
                'name': 'Sarah Johnson',
                'age': 31,
                'address': '321 Maple Lane, Hamletville, ST 98765',
                'fingerprint': 'sarah_unique_fingerprint_004'
            },
            {
                'name': 'David Kim',
                'age': 39,
                'address': '654 Birch Street, Cityburg, ST 43210',
                'fingerprint': 'david_unique_fingerprint_005'
            },
            {
                'name': 'Sudarsan Kumar',
                'age' : 21,
                'address' : '780/4,shivaji nagar,r.k.theater opp,salem - 3',
                'fingerprint': 'sudarsan_unique_fingerprint_006'
            },
            {
                'name': 'Kriksha',
                'age': 20,
                'address' : '654 Birch Street, Cityburg, ST 43210',
                'fingerprint' : 'kriksha_unique_fingerprint_007'
            }
        ]

        registered_voters = []
        for voter in sample_voters:
            registration = self.register_voter(
                name=voter['name'],
                age=voter['age'],
                address=voter['address'],
                fingerprint=voter['fingerprint']
            )
            if registration:
                registered_voters.append(registration)
        
        return registered_voters

    def display_all_voters(self):
        """
        Display all registered voters
        """
        self.cursor.execute('''
        SELECT voter_id, name, age, address, fingerprint_hash
        FROM voters
        ''')
        
        voters = self.cursor.fetchall()
        print("\n--- Registered Voters ---")
        for voter in voters:
            print(f"Voter ID: {voter[0]}")
            print(f"Name: {voter[1]}")
            print(f"Age: {voter[2]}")
            print(f"Address: {voter[3]}")
            print(f"Fingerprint: {voter[4]}")
            print("---")

    def close_connection(self):
        """Close database connection"""
        self.conn.close()

def main():
    # Create database instance
    db = VoterBlockchainDatabase()
    
    # Insert sample voters
    registered_voters = db.insert_sample_voters()
    
    # Display all registered voters
    db.display_all_voters()
    
    # Close database connection
    db.close_connection()

if __name__ == "__main__":
    main()