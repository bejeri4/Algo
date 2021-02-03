# https://www.interviewbit.com/problems/lru-cache/

class Node:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None


class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.dct = dict()
        self.head = None
        self.tail = None

    # @return an integer
    def get(self, key):
        result = -1
        if key in self.dct:
            result, node = self.dct[key]
            self.updateOrder(node, key)
        return result
        
    def updateOrder(self, node, key):
        if self.head.key == key:
            return
        if self.tail.key == key:
            self.tail = self.tail.prev
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.next = self.head
        self.head.prev = node
        self.head = node
        
    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        node = None
        if key in self.dct:
            _, node = self.dct[key]
        else:
            node = Node(key)
            if self.head:
                node.next = self.head
                self.head.prev = node
                self.head = node
            else:
                self.head = node
                self.tail = node
        self.dct[key] = [value, node]
        self.updateOrder(node, key)
        self.removeLastIfNeeded()
            
    def removeLastIfNeeded(self):
        if len(self.dct) == self.capacity + 1:
            del self.dct[self.tail.key]
            self.tail = self.tail.prev
            self.tail.next = None
        
        
