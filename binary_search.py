class BinarySearch:

    def search(self, array, value):
        return self.binarySearch(value, array, 0, len(array) - 1)

    def binarySearch(self, value, array, start, end):

        if start > end:
            return -1

        middle = (end + start) / 2

        if array[middle] < value:
            return self.binarySearch(value, array, middle + 1, end)

        if array[middle] > value:
            return self.binarySearch(value, array, start, middle - 1)

        return middle


def main():
    s = BinarySearch()
    print s.search([1, 2, 3, 4, 5, 6], 7)

if __name__ == '__main__':
    main()