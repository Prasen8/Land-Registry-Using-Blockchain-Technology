import json
from flask import Flask, render_template, request
from datetime import datetime
from hashlib import sha256

# Define the file path for storing the blockchain data
BLOCKCHAIN_FILE = 'blockchain.json'

app = Flask(__name__)

# list to store blockchain
blockchain = []

# Function to save the blockchain to a JSON file
def save_blockchain():
    """Saves the blockchain list to a file."""
    # Convert list of objects to list of dictionaries for JSON serialization
    serializable_blockchain = []
    for record in blockchain:
        serializable_blockchain.append({
            'timestamp': record.timestamp.isoformat(),  # Convert datetime object to string
            'name': record.name,
            'age': record.age,
            'uid': record.uid,
            'land': record.land,
            'previous_hash': record.previous_hash,
            'hash': record.hash
        })
    with open(BLOCKCHAIN_FILE, 'w') as f:
        json.dump(serializable_blockchain, f, indent=4)

# Function to load the blockchain from a JSON file
def load_blockchain():
    """Loads the blockchain list from a file if it exists."""
    global blockchain
    try:
        with open(BLOCKCHAIN_FILE, 'r') as f:
            data = json.load(f)
            # Recreate PatientRecord objects from the loaded data
            blockchain = []
            for record_data in data:
                record = PatientRecord(
                    name=record_data['name'],
                    uid=record_data['uid'],
                    age=record_data['age'],
                    land=record_data['land']
                )
                record.timestamp = datetime.fromisoformat(record_data['timestamp'])
                record.previous_hash = record_data['previous_hash']
                # The hash is recalculated to ensure integrity
                record.hash = record.calculate_hash()
                blockchain.append(record)
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file doesn't exist or is corrupted, start with an empty blockchain
        blockchain = []

# Patient record class
class PatientRecord:
    def __init__(self, name, uid, age, land):
        self.timestamp = datetime.now()
        self.name = name
        self.age = age
        self.uid = uid
        self.land = land
        self.previous_hash = None
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """Calculates the SHA256 hash of the record's data."""
        # Include previous hash in the data to be hashed
        hash_data = f"{self.timestamp}{self.name}{self.age}{self.uid}{self.land}{self.previous_hash}"
        return sha256(hash_data.encode()).hexdigest()
    
    # This method is not needed anymore as the hash is calculated inside __init__
    # def calculate_previous_hash(self):
    #     if len(blockchain) > 0:
    #         return blockchain[-1].hash
    #     else:
    #         return None

# to add new record to blockchain
@app.route('/add_record', methods=['POST'])
def add_record():
    name = request.form['name']
    age = request.form['age']
    land = request.form['land']
    uid = request.form['uid']

    # Create a new patient record
    record = PatientRecord(name, uid, age, land)

    # Adding the patient record to the blockchain
    if len(blockchain) > 0:
        record.previous_hash = blockchain[-1].hash
    
    # Recalculate hash after setting previous_hash
    record.hash = record.calculate_hash()
    blockchain.append(record)
    
    # Save the updated blockchain to the file
    save_blockchain()

    return f'Record added to blockchain successfully. Your User ID - {uid}'

# getting patient record from blockchain
@app.route('/get_records', methods=['GET'])
def get_record():
    uid = request.args.get('uid')
    for block in blockchain:
        # Note: uid from form is a string, so cast block.uid to string for comparison
        if str(block.uid) == uid:
            return render_template('record.html', record=block)
    return 'Record not found.'

# displaying whole blockchain
@app.route('/view_blockchain', methods=['GET'])
def view_blockchain():
    return render_template('blockchain.html', blockchain=blockchain)

@app.route('/get_patient_history', methods=['GET'])
def get_patient_history():
    pass

@app.route('/get_history', methods=['GET'])
def get_history():
    uid = request.args.get('uid')
    history = [block for block in blockchain if str(block.uid) == uid]
    
    if history:
        return render_template('patient_records.html', all_records=history)
    else:
        return 'Record not found.'
    
# returning landing page
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Load the blockchain from file when the application starts
    load_blockchain()
    app.run(debug=True)
