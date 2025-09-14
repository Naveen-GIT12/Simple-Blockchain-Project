import unittest
from src.simple_blockchain import Blockchain

class TestBlockchain(unittest.TestCase):
    def test_chain_validity(self):
        bc = Blockchain(difficulty=2)
        bc.add_block("Test Block")
        self.assertTrue(bc.is_chain_valid())

    def test_tampering(self):
        bc = Blockchain()
        bc.add_block("Legit Block")
        bc.chain[1].data = "Tampered"
        self.assertFalse(bc.is_chain_valid())

if __name__ == '__main__':
    unittest.main()
