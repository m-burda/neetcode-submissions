class LRUCache:
    """
    use a hashmap to map keys to nodes.
    values are stored in a doubly linked list
    keep track of head and tail
    on get/put, move the node to the front, update the head
    track size. if capacity exceeded, move tail to head, update hashmap
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mapping = {}

        self.lru = ListNode()
        self.mru = ListNode()
        self.lru.next = self.mru
        self.mru.prev = self.lru

    def get(self, key: int) -> int:
        node = self.mapping.get(key)
        if node:
            self._evict(node)
            self._insert(node)
        return node.value if node else -1

    def put(self, key: int, value: int) -> None:
        node = self.mapping.get(key)
        if node:
            evicted = self._evict(node)
            node.value = value
            self._insert(node)
        else:
            if len(self.mapping) == self.capacity:
                evicted = self.lru.next
                self._evict(evicted)
                del self.mapping[evicted.key]
            
            node = ListNode(key, value)
            self._insert(node)
        
        self.mapping[key] = node
    
    def _insert(self, node: ListNode):
        node.prev = self.mru.prev
        self.mru.prev.next = node
        self.mru.prev = node
        node.next = self.mru

    def _evict(self, node: ListNode):
        node.next.prev = node.prev
        node.prev.next = node.next

class ListNode:
    def __init__(self, key = None, value: int = None, next = None, prev = None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev
