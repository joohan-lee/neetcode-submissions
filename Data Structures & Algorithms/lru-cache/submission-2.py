class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

        self.cache = {} # key-value(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # Move used node to tail
        node = self.cache[key]
        self._remove(node)
        self._insert(node)
        
        return node.val

    def put(self, key: int, value: int) -> None:
        # If key exists
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            # Move used node to end
            self._remove(node)
            self._insert(node)
            return
        
        # If key does not exists, create a new one
        # If capacity exceeds, remove least used one
        if self.capacity == len(self.cache):
            lru = self.head.next
            del self.cache[lru.key]
            self._remove(lru)
        
        self.cache[key] = Node(key, value)
        self._insert(self.cache[key])
    
    def _insert(self, node):
        # add node to tail
        node.prev = self.tail.prev
        node.prev.next = node
        node.next = self.tail
        self.tail.prev = node
    
    def _remove(self, node):
        # remove node
        node.prev.next = node.next
        node.next.prev = node.prev

