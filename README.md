![1_mwpuwHSsNIlIirvWdjgIbw](https://github.com/user-attachments/assets/3014f481-ede1-4d7b-9c59-9bc8eb920d32)

# 🏠 Land Registry Using Blockchain Technology
# 📖 Overview :
This project is a web-based decentralized land registry system built using Blockchain technology. It provides a transparent, immutable, and secure method to record and verify land ownership and transaction history.
Developed with Python (Flask), this application simulates how blockchain can revolutionize traditional land registration systems by ensuring trust and preventing data manipulation.

# ✨ Features :
🧱 Immutable Land Records:
Each land record is stored as a “block” in the blockchain. Once added, it cannot be altered or deleted, ensuring complete data integrity.

# 🔗 Tamper-Proof History:
Every block includes a cryptographic hash of the previous block. Any modification breaks the chain, making tampering instantly detectable.

# 💻 User-Friendly Interface:
Intuitive web interface to:

# Add new land records
Search and view specific records by unique ID
Visualize the entire blockchain

# 💾 Persistent Data Storage:
The blockchain is saved in a local blockchain.json file, preserving all records even after restarting the app.

# 📜 Full Blockchain Visualization:
A dedicated page displays all blocks, showing timestamps, owner details, current hash, and previous hash for transparency.

# 🧠 System Architecture :
User Interface (Flask + HTML/CSS)
        ↓
Flask Application (Backend)
        ↓
Blockchain Class (Python)
        ↓
Hashing Algorithm (SHA-256 via hashlib)
        ↓
Persistent Storage (JSON File)

# 💻 Technologies Used :
Technology	Purpose
Python	Core programming logic
Flask	Web framework for handling routes and rendering templates
Jinja2	Templating engine for dynamic web pages
hashlib	Implements SHA-256 cryptographic hashing
HTML/CSS	Frontend structure and styling
JSON	Local persistent data storage

# 🔐 How SHA-256 Ensures Data Integrity :

In this project, every land record is stored as a block that contains details like owner name, land ID, and timestamp.
To make sure the data inside each block cannot be tampered with, I’ve implemented SHA-256 cryptographic hashing.

🧩 How It Works:

When a new block is created, all its data (like land details + timestamp + previous block hash) is passed through the SHA-256 algorithm.

This algorithm converts the input data into a unique 64-character hash (a digital fingerprint).

Even the smallest change in the block’s data (like a single character) will completely change the hash value.

Each block also stores the hash of the previous block, creating a linked chain.

If anyone tries to modify a past record, the hashes break the chain — instantly revealing tampering.

# 🧠 Why It’s Important:
✅ Maintains data integrity — once recorded, data cannot be altered.
✅ Makes the system transparent and trustworthy without needing a central authority.
✅ Acts as a digital signature for each block, securing land ownership records permanently.



# Prasen Nimje
# 🚀 Final Year AI & DS Student 
