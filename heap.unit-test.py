import unittest
from heap import Heap

class HeapTest(unittest.TestCase):

    def setUp(self):
        self.heap = Heap()

    def tearDown(self):
        del self.heap

    def testInsertSingle(self):
        self.heap.insert(1)
        self.assertEqual([1], self.heap.array)

    def testInsertMultiple(self):
        self.heap.insert(1)
        self.heap.insert(2)
        self.assertEqual([2, 1], self.heap.array)

        self.heap.insert(3)
        self.assertEqual([3, 1, 2], self.heap.array)

    def testGetMax(self):
        self.heap.insert(1)
        self.heap.insert(5)
        self.heap.insert(100)
        self.heap.insert(20)

        self.assertEqual(self.heap.getMax(), 100)

    def testGetSize(self):
        self.assertEqual(self.heap.getSize(), 0)

        self.heap.insert(1)
        self.heap.insert(5)
        self.assertEqual(self.heap.getSize(), 2)

    def testIsEmpty(self):
        self.assertTrue(self.heap.isEmpty())

        self.heap.insert(5)
        self.assertFalse(self.heap.isEmpty())

    def testExtractMax(self):
        self.heap.insert(1)
        self.assertEqual(self.heap.extractMax(), 1)
        self.assertNotEqual(self.heap.getMax(), 1)

if __name__ == '__main__':
    unittest.main()