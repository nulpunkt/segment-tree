import unittest
from tree import SegmentTree, Range

class TestSegementTree(unittest.TestCase):
    def test_construct_terminal(self):
        tree = SegmentTree([1,2])
        self.assertEquals(3, tree.sum(0, 1))
    
    def test_construct_mini_tree(self):
        tree = SegmentTree([1,2,3,4])
        self.assertEquals(10, tree.sum(0, 3))

    def test_partial_sum(self):
        tree = SegmentTree([1,2,3,4,12,13])
        self.assertEquals(3, tree.sum(0, 1))
        self.assertEquals(7, tree.sum(2, 3))
        self.assertEquals(21, tree.sum(1, 4))
    
    def test_set_leaf(self):
        tree = SegmentTree([1,2,3,4])
        self.assertEquals(2, tree.sum(1, 1))
        tree.set(1, 10)
        self.assertEquals(10, tree.sum(1, 1))

    def test_set_internal(self):
        tree = SegmentTree([1,2,3,4])
        self.assertEquals(10, tree.sum(0, 3))
        tree.set(1, 10)
        self.assertEquals(11, tree.sum(0, 1))
        self.assertEquals(18, tree.sum(0, 3))

class TestRange(unittest.TestCase):
    def test_split(self):
        range = Range(3,5)
        expected_split = (Range(3,4), Range(5,5))
        self.assertEquals(expected_split, range.split())
    
    def test_contains(self):
        outer = Range(0,5)
        inner = Range(2,3)
        self.assertTrue(outer.contains(inner))
    
    def test_partially_contains(self):
        outer = Range(3,5)
        inner = Range(2,3)
        self.assertTrue(outer.partially_contains(inner))
        inner = Range(3,3)
        self.assertTrue(outer.partially_contains(inner))

if __name__ == "__main__":
    unittest.main()
