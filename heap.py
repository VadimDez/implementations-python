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
        parent = index / 2

        if parent < 0 & parent > self.size:
            return

        if self.array[parent] < self.array[index]:
            self.swap(index, parent)
            # continue sift up
            self.siftUp(parent)

    def getMax(self):
        return self.array[0]

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def extractMax(self):
        max = self.getMax()
        self.array[0] = self.array[self.size - 1]
        self.size -= 1
        return max

    def siftDown(self, index):
        leftIndex = (index + 1) * 2
        rightIndex = leftIndex + 1
        biggerThanLeft = self.array[index] > self.array[leftIndex]
        biggerThanRight = self.array[index] > self.array[rightIndex]

        if biggerThanLeft & biggerThanRight:
            if self.array[leftIndex] > self.array[rightIndex]:
                self.swap(leftIndex, index)
                self.siftDown(leftIndex)
                return

            self.swap(index, rightIndex)
            self.siftDown(rightIndex)
            return

        if biggerThanRight:
            self.swap(index, rightIndex)
            self.siftDown(leftIndex)
            return

        if biggerThanLeft:
            self.swap(index, leftIndex)
            self.siftDown(leftIndex)
            return

    # swap two elements
    def swap(self, indexA, indexB):
        tmp = self.array[indexA]
        self.array[indexA] = self.array[indexB]
        self.array[indexB] = tmp