class Node:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
class LFUCache:

    def __init__(self, capacity: int):
        """
        Initializes the object with the capacity
        """
        self.capacity = capacity
        self.useCounter = {} # To track the frequency
        self.keyToNode = {} # To get a node in O(1) time.
        
        # Use doubly-linked list to insert a node at the end in O(1) time.
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        """
        Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
        """
        # print(f'{key=}, {self.keyToNode=}, {self.useCounter=}')
        # Early return
        if key not in self.keyToNode:
            return -1
        
        # Count up the frequency at key
        self.useCounter[key] += 1
        
        # Move the node at key to the end (LRU)
        node = self.keyToNode[key]
        self._removeNode(node)
        self._insertNodeToEnd(node)

        # Return value
        return node.val
        

    def put(self, key: int, value: int) -> None:
        """
        Update the value of the key if present, or inserts the key if not already present.
        When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item.
        If tie, the least recently used key would be invalidated.
        """
        # print(f'{key=}, {self.keyToNode=}, {self.useCounter=}')
        if key in self.keyToNode:
            # Update
            node = self.keyToNode[key]
            node.val = value

            self.useCounter[key] += 1
            self._removeNode(node)
            self._insertNodeToEnd(node)

        else:
            # Insert
            if len(self.keyToNode) == self.capacity:
                # Remove least frequently and least recently used one
                min_freq = float('inf')
                for k, node in self.keyToNode.items():
                    min_freq = min(min_freq, self.useCounter[k])
                
                min_freq_nodes = set()
                for k, node in self.keyToNode.items():
                    if self.useCounter[k] == min_freq:
                        min_freq_nodes.add(node)
                
                curr = self.head
                while curr:
                    if curr in min_freq_nodes:
                        self._removeNode(curr)
                        del self.useCounter[curr.key]
                        del self.keyToNode[curr.key]
                        break
                    curr = curr.next
                
            node = Node(key=key, val=value)
            self.keyToNode[key] = node
            self._insertNodeToEnd(node)

            self.useCounter[key] = self.useCounter.get(key, 0) + 1
    
    def _removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _insertNodeToEnd(self, node):
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
        



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)