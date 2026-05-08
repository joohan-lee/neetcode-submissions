class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key-node

        # Doubly Linked List to easily append a node to the end.
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def _remove(self, node):
        # remove node from doubly linked list
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _insert(self, node):
        # insert node at the end of doubly linked list
        node.prev = self.right.prev
        self.right.prev.next = node
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        # Move the used key to the end
        node = self.cache[key]
        self._remove(node)

        self._insert(node)
        
        # Return value
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._insert(node)
            return

        # if it is already capacity, remove first elem (least recently used)
        if len(self.cache) == self.capacity:
            lru = self.left.next
            del self.cache[lru.key]
            self._remove(lru)
        
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._insert(new_node)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)