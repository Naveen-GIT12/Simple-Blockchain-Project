# 🚀 Simple Blockchain Project

A Python-based blockchain simulator demonstrating **core blockchain principles**, enhanced with **Proof-of-Work mining**, a **Flask-powered REST API**, and automated **unit testing**.  

This project is designed as an **educational tool** to showcase how blocks, hashes, and validation create a secure, immutable ledger.  

---

## 📂 Project Structure
```
Simple-Blockchain-Project/
│── src/
│   └── simple_blockchain.py   
│── tests/
│   └── test_blockchain.py     
│── docs/
│   └── report.md             
│── .gitignore                 
│── requirements.txt          
│── Dockerfile                 
│── README.md                  
```

---

## ⚙️ Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/Simple-Blockchain-Project.git
cd Simple-Blockchain-Project
```

### 2. Create Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### Run the Blockchain Server
```bash
python src/simple_blockchain.py
```

By default, the server runs at:  
👉 `http://127.0.0.1:5000`

### REST API Endpoints
- **Mine a new block**
  ```bash
  curl -X POST http://127.0.0.1:5000/mine        -H "Content-Type: application/json"        -d '{"data":"My first transaction"}'
  ```
  ✅ Response includes the new block details.

- **Fetch the entire blockchain**
  ```bash
  curl http://127.0.0.1:5000/chain
  ```
  ✅ Returns all blocks, chain length, and validity.

---

## 🧪 Running Tests
To ensure integrity:
```bash
python -m unittest discover tests
```
- Tests blockchain validity.  
- Ensures tampering is detected.  

---

## ✅ Features
- 📦 **Block creation & chaining** with metadata (index, timestamp, data, previous hash).  
- 🔒 **SHA-256 hashing** for immutability.  
- ⛏️ **Proof-of-Work mining** (adjustable difficulty).  
- 🌐 **Flask REST API** for interacting with blockchain.  
- 🧪 **Unit tests** for reliability.  
- 🐳 **Dockerized deployment** for portability.  

---

## 🌟 Future Enhancements
- 🤝 Peer-to-peer networking (multiple nodes maintaining the chain).  
- 🗳️ Consensus algorithms (Proof-of-Stake, Delegated PoS, etc.).  
- 💼 Wallet & transaction system with public/private keys.  
- 📊 Web dashboard for visualizing the blockchain.  
- 🔗 Smart contract demo for advanced use cases.  

---

## 📸 Example Output

When mining blocks:
```
Mining block 1...
Block mined: 000af91e92f57...
Mining block 2...
Block mined: 000bd12a4f8d...
```

Blockchain validation:
```
Blockchain valid? True
```

---

## 🐳 Docker Deployment
Build and run in a container:
```bash
docker build -t blockchain .
docker run -p 5000:5000 blockchain
```

---

## 📚 References
- [Bitcoin Whitepaper – Satoshi Nakamoto](https://bitcoin.org/bitcoin.pdf)  
- [Flask Documentation](https://flask.palletsprojects.com/)  
- [Python hashlib module](https://docs.python.org/3/library/hashlib.html)  

---
