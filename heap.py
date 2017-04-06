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
        return self.array[0]

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def extractMax(self):
        max = self.getMax()
        self.swap(0, self.size - 1)
        self.size -= 1
        self.siftDown(0)
        return max

    def siftDown(self, index):
        # +1 and +2 because array starts from 0
        leftIndex = index * 2 + 1
        rightIndex = leftIndex + 1
        print "leftIndex", leftIndex
        print "rightIndex", rightIndex

        try:
            biggerThanLeft = self.array[index] > self.array[leftIndex]
        except IndexError:
            biggerThanLeft = False

        try:
            biggerThanRight = self.array[index] > self.array[rightIndex]
        except IndexError:
            biggerThanRight = False

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