class BinHeap:
    def __init__(self):
        self.heapList = []
        self.currentSize = 0

    # General rule:
    # Position of root = p
    # Position of left child (relative to p) = 2p
    # Position of right child (relative to p) = 2p + 1

    def percUp(self, i):
        while i // 2 > 0:
            # Floor or 2p + 1 == p
            # Travel up and check every root
            # If any of the child > root, then swap their position
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    # The root of the tree must be the smallest
    # item in the tree

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self, i):
        # If there's no right child
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            # Check left or right child is smaller
            if self.heapList[i * 2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        # Because the first number of your heapList is 0
        retval = self.heapList[1]
        # Replace the root with the last item of the tree
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        # Remove the last item (which should be the smallest
        # number)
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1
