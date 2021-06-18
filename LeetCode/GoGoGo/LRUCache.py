class LRUCache:
    
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.head = self.Node(None, None)
        self.tail = self.Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dct = dict()
    
    def get(self, key: int) -> int:
        if key in self.dct:
            node = self.dct[key]
            self.moveToHead(node)
            return node.value
        else:
            return -1
        
    def moveToHead(self, node):
        self.removeNode(node)
        self.addNode(node)
        
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def addNode(self, node):
        self.head.next.prev = node
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        
    def put(self, key: int, value: int) -> None:
        if key in self.dct:
            node = self.dct[key]
            node.value = value
            self.moveToHead(node)
        else:
            node = self.Node(key, value)
            self.dct[key] = node
            self.addNode(node)
            self.size += 1
            if self.size > self.capacity:
                self.size -= 1
                k = self.tail.prev.key
                self.removeNode(self.tail.prev)
                del self.dct[k]
            
            
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
