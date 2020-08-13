import unittest
from search import linear_search, binary_search

class TestSearch(unittest.TestCase):

    def test_search(self):
        data = [1, 2, 3, 5, 6, 12, 7, 4, 8]
        self.assertEqual(linear_search(data, 6), 4)
        self.assertEqual(linear_search(data, 10),  -1)
        self.assertEqual(linear_search(data, 2), 1)
        self.assertEqual(linear_search(data, 8), 8)
        self.assertEqual(linear_search(data, 1), 0)

    def test_searchChar(self):
        data = ['t', 'a', 'b', 'l', 'e']
        self.assertEqual(linear_search(data, 'a'), 1)
        self.assertEqual(linear_search(data, 's'), -1)
        self.assertEqual(linear_search(data, 'e'), 4)

class TestBinarySearch(unittest.TestCase):

    def test_search(self):
        data = [1, 2, 3, 4, 5, 6, 7, 8, 12]
        self.assertEqual(binary_search(data, 9), -1)
        self.assertEqual(binary_search(data, 3), 2)
        self.assertEqual(binary_search(data, 1), 0)
        self.assertEqual(binary_search(data, 7), 6)
    
    def test_searchChar(self):
        data = ['a', 'b', 'e', 'l', 't']
        self.assertEqual(binary_search(data, 'a'), 0)
        self.assertEqual(linear_search(data, 'u'), -1)
    
if __name__ == "__main__":
    unittest.main()