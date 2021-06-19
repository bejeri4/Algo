class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.elems = []
        

    def addNum(self, num: int) -> None:
        i = bisect_left(self.elems, num)
        self.elems.insert(i, num)

    def findMedian(self) -> float:
        if len(self.elems) % 2 == 1:
            return self.elems[len(self.elems) // 2]
        else:
            return (self.elems[(len(self.elems) - 1) // 2] + self.elems[len(self.elems) // 2]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
