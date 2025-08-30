# Simple Blockchain Simulator

This is a very basic, single-file Python script that simulates a blockchain.
It demonstrates the core concepts of:
- **Blocks:** Data containers.
- **Hashing:** Generating a unique fingerprint for each block.
- **Chaining:** Each block referencing the hash of the previous block, creating an immutable ledger.

## How it works

The script creates a "genesis block" (the first block) and then adds a few subsequent blocks. Each new block includes data (simulated transactions) and the hash of the block that came before it. This interlocking mechanism is what makes a blockchain secure and tamper-proof.

## How to Run (via GitHub Codespaces)

1.  **Create a Codespace:** Follow the instructions below to open this repository in a GitHub Codespace.
2.  **Open Terminal:** In the Codespace, open a new terminal.
3.  **Run the script:**
    ```bash
    python3 simple_blockchain.py
    ```

The output in the terminal will show the details of each block as it's added to the simulated chain, along with a final check of the chain's integrity.

## OUTPUT

<img width="1919" height="1079" alt="OUTPUT" src="https://github.com/user-attachments/assets/0f524589-9ffd-4fb9-8b27-fbaa066d51bc" />


