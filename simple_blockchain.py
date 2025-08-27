import hashlib
import datetime

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Concatenate all block properties to create a unique string
        block_string = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(block_string.encode()).hexdigest()

def create_genesis_block():
    # The first block in the chain (index 0)
    return Block(0, datetime.datetime.now(), "Genesis Block", "0")

def create_new_block(last_block, data):
    # Create a new block, linking it to the previous one
    this_index = last_block.index + 1
    this_timestamp = datetime.datetime.now()
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, data, this_hash)

if __name__ == "__main__":
    # 1. Create the blockchain and add the genesis block
    blockchain = [create_genesis_block()]
    previous_block = blockchain[0]

    # 2. Add a few more blocks
    num_blocks_to_add = 5

    print("--- Building Blockchain ---")
    for i in range(0, num_blocks_to_add):
        block_data = f"Transaction #{i+1} Data - Value Sent: {10 * (i+1)} INR"
        new_block = create_new_block(previous_block, block_data)
        blockchain.append(new_block)
        previous_block = new_block
        print(f"Block #{new_block.index} added:")
        print(f"  Timestamp: {new_block.timestamp}")
        print(f"  Data: {new_block.data}")
        print(f"  Hash: {new_block.hash}")
        print(f"  Previous Hash: {new_block.previous_hash}\n")

    print("--- Blockchain Built ---")
    print(f"Total blocks in chain: {len(blockchain)}")

    # 3. Verify chain integrity (optional check)
    print("\n--- Verifying Chain Integrity ---")
    is_valid = True
    for i in range(1, len(blockchain)):
        current = blockchain[i]
        previous = blockchain[i-1]
        if current.previous_hash != previous.hash:
            is_valid = False
            print(f"ERROR: Block {current.index} previous hash does not match Block {previous.index} hash!")
        if current.hash != current.calculate_hash():
            is_valid = False
            print(f"ERROR: Block {current.index} has an invalid hash!")
    if is_valid:
        print("Blockchain integrity is **VALID**.")
    else:
        print("Blockchain integrity is **INVALID**.")

