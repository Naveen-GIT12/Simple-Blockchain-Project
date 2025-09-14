# Simple Blockchain Project 🚀

A Python-based blockchain simulator with **Proof-of-Work**, **Flask REST API**, and **integrity validation**.

## 📂 Project Structure
```
src/        -> Blockchain core
tests/      -> Unit tests
docs/       -> Documentation/report
```

## ⚙️ Setup

### Clone the repo
```bash
git clone https://github.com/your-username/Simple-Blockchain-Project.git
cd Simple-Blockchain-Project
```

### Install dependencies
```bash
pip install -r requirements.txt
```

## ▶️ Usage

Run the blockchain server:
```bash
python src/simple_blockchain.py
```

### Endpoints
- `POST /mine` → Add a new block  
- `GET /chain` → Fetch the entire blockchain

## ✅ Features
- Block creation & chaining
- SHA-256 hashing
- Proof-of-Work (mining)
- REST API (Flask)
- Unit tests
- Dockerized deployment

## 🌟 Future Enhancements
- Peer-to-peer networking
- Consensus algorithms
- Smart contract demo
