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

    def testExtractMaxMultiple(self):
        self.heap.insert(1)
        self.heap.insert(6)
        self.heap.insert(2)
        self.heap.insert(8)

        self.assertEqual(self.heap.extractMax(), 8)
        self.assertNotEqual(self.heap.getMax(), 8)
        self.assertEqual(self.heap.array[self.heap.size], 8)

        self.assertEqual(self.heap.extractMax(), 6)
        self.assertNotEqual(self.heap.getMax(), 6)
        self.assertEqual(self.heap.array[self.heap.size], 6)

    def testRemove(self):
        self.heap.insert(5)
        self.heap.remove(0)
        self.assertEqual(self.heap.array, [])

        self.heap.insert(3)
        self.heap.insert(2)
        self.heap.remove(1)
        self.assertEqual(self.heap.array, [3])

    def testHeapify(self):
        self.heap.heapify([2, 5])
        self.assertEqual(self.heap.array, [5, 2])

        self.heap.heapify([2, 5, 6, 1, 4])
        self.assertEqual(self.heap.array, [6, 5, 2, 1, 4])

    def testHeapSort(self):
        sortedArray = self.heap.sort([5, 1, 3, 6, 8, 4])
        self.assertEqual(sortedArray, [1, 3, 4, 5, 6, 8])

        sortedArray = self.heap.sort([5, 4, 3, 2, 1])
        self.assertEqual(sortedArray, [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()