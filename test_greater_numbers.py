import unittest
from greater_numbers import nextGreaterElement



class TestNextGreaterElement(unittest.TestCase):
    def test_example1(self):
        nums1 = [4, 1, 2]
        nums2 = [1, 3, 4, 2]
        expected = [-1, 3, -1]
        self.assertEqual(nextGreaterElement(nums1, nums2), expected)

    def test_example2(self):
        nums1 = [2, 4]
        nums2 = [1, 2, 3, 4]
        expected = [3, -1]
        self.assertEqual(nextGreaterElement(nums1, nums2), expected)

    def test_all_greater(self):
        nums1 = [1, 2, 3]
        nums2 = [3, 2, 1]
        expected = [-1, -1, -1]
        self.assertEqual(nextGreaterElement(nums1, nums2), expected)

    def test_no_elements(self):
        nums1 = []
        nums2 = []
        expected = []
        self.assertEqual(nextGreaterElement(nums1, nums2), expected)

    def test_single_element(self):
        nums1 = [1]
        nums2 = [1, 2, 3, 4]
        expected = [2]
        self.assertEqual(nextGreaterElement(nums1, nums2), expected)

    def test_larger_elements(self):
        nums1 = [4, 1, 2, 3]
        nums2 = [4, 3, 2, 1, 5]
        expected = [5, 5, 5, 5]
        self.assertEqual(nextGreaterElement(nums1, nums2), expected)

if __name__ == "__main__":
    unittest.main(verbosity=2)