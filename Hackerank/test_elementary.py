import unittest
from elementary import getMinMoves

class TestElementary(unittest.TestCase):
    def test_getMinMoves(self):
        # Test case 1
        word1 = "adabacaea"
        expected1 = 3
        self.assertEqual(getMinMoves(word1), expected1)

        # Test case 2
        word2 = "cbaa"
        expected2 = 1
        self.assertEqual(getMinMoves(word2), expected2)

        # Test case 3
        word3 = "abcde"
        expected3 = 0
        self.assertEqual(getMinMoves(word3), expected3)

        # Test case 4
        word4 = "aabbbccc"
        expected4 = 6
        self.assertEqual(getMinMoves(word4), expected4)

if __name__ == '__main__':
    unittest.main()