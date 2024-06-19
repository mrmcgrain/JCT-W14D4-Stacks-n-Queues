import unittest

from circular_array import nextGreaterElements

class TestNextGreaterElements(unittest.TestCase):

    def test_example_cases(self):
        # Test with example cases
        self.assertEqual(nextGreaterElements([1, 2, 1]), [2, -1, 2])
        self.assertEqual(nextGreaterElements([1, 2, 3, 4, 3]), [2, 3, 4, -1, 4])
        self.assertEqual(nextGreaterElements([5, 4, 3, 2, 1]), [-1, 5, 5, 5, 5])
        self.assertEqual(nextGreaterElements([1, 2, 3, 2, 1]), [2, 3, -1, 3, 2])
        self.assertEqual(nextGreaterElements([2, 1, 2, 4, 3]), [4, 2, 4, -1, 4])

    def test_edge_cases(self):
        # Test with edge cases
        self.assertEqual(nextGreaterElements([]), [])
        self.assertEqual(nextGreaterElements([1]), [-1])
        self.assertEqual(nextGreaterElements([1, 1, 1, 1]), [-1, -1, -1, -1])
        self.assertEqual(nextGreaterElements([1, 2, 3, 4]), [2, 3, 4, -1])
        self.assertEqual(nextGreaterElements([4, 3, 2, 1]), [-1, 4, 4, 4])

    def test_custom_cases(self):
        # Test with custom cases
        self.assertEqual(nextGreaterElements([1, 3, 2, 4]), [3, 4, 4, -1])
        self.assertEqual(nextGreaterElements([2, 4, 3, 1]), [4, -1, 4, 2])
        self.assertEqual(nextGreaterElements([1, 1, 2, 2]), [2, 2, -1, -1])
        self.assertEqual(nextGreaterElements([6, 8, 0, 1, 3]), [8, -1, 1, 3, 6])

if __name__ == '__main__':
    unittest.main(verbosity=2)