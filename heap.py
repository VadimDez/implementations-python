class Heap:

    def __init__(self):
        self.array = []
        self.size = 0

    # insert to the heap
    def insert(self, value):
        self.array.append(value)
        self.size += 1
        self.siftUp(self.size - 1)

    # sift up item at index
    def siftUp(self, index):
        # -1 because array index starts from 0
        tmpIndex = index - 1

        if tmpIndex < 0:
            tmpIndex = 0

        parent = tmpIndex / 2

        if parent < 0 & parent > self.size:
            return

        if self.array[parent] < self.array[index]:
            self.swap(index, parent)
            # continue sift up
            self.siftUp(parent)

    def getMax(self):
        if self.size <= 0:
            return
        return self.array[0]

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def extractMax(self):
        if self.size <= 0:
            return

        max = self.getMax()
        self.swap(0, self.size - 1)
        self.size = self.size - 1
        self.siftDown(0)
        return max

    def siftDown(self, index):
        # +1 and +2 because array starts from 0
        leftIndex = index * 2 + 1
        rightIndex = leftIndex + 1
        smallerThanRight = False
        smallerThanLeft = False

        if leftIndex < self.size:
            smallerThanLeft = self.array[index] < self.array[leftIndex]

        if rightIndex < self.size:
            smallerThanRight = self.array[index] < self.array[rightIndex]

        if smallerThanLeft & smallerThanRight:
            if self.array[leftIndex] > self.array[rightIndex]:
                self.swap(leftIndex, index)
                self.siftDown(leftIndex)
                return

            self.swap(index, rightIndex)
            self.siftDown(rightIndex)
            return

        if smallerThanRight:
            self.swap(index, rightIndex)
            self.siftDown(leftIndex)
            return

        if smallerThanLeft:
            self.swap(index, leftIndex)
            self.siftDown(leftIndex)
            return

    # swap two elements
    def swap(self, indexA, indexB):
        tmp = self.array[indexA]
        self.array[indexA] = self.array[indexB]
        self.array[indexB] = tmp

    def heapify(self, array):
        self.array = array
        self.size = len(array)

        for i in range((self.size - 1) / 2, -1, -1):
            self.siftDown(i)

    def sort(self, array):
        self.heapify(array)

        for i in range(0, self.size - 1):
            self.extractMax()

        return self.array

    # remove item from heap by index
    def remove(self, index):

        if index == 0 & self.size == 1:
            self.array = []
            self.size = 0
            return

        self.array[index] = self.array[self.size - 1]
        del self.array[self.size - 1]
        self.size -= 1
        self.siftDown(index)