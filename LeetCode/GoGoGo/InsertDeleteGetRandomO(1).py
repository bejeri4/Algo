import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dct = dict()
        self.arr = []
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dct:
            return False
        else:
            self.arr.append(val)
            self.dct[val] = len(self.arr) - 1
            return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dct:
            index = self.dct[val]
            del self.dct[val]
            self.arr[index] = self.arr[-1]
            self.arr.pop()
            if index < len(self.arr):
                self.dct[self.arr[index]] = index
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        i = random.randint(0, len(self.arr) - 1)
        return self.arr[i]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
