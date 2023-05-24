class DLinkedNode:
    def __init__(self): 
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}
        self.size = 0

    def _insert(self, node): 
        node.prev = self.head
        node.next = self.head.next 
        self.head.next.prev = node 
        self.head.next = node 
    
    def _remove(self, node): 
        node.next.prev = node.prev 
        node.prev.next = node.next

    def _move_to_front(self, node):
        self._remove(node)
        self._insert(node) 

    def _remove_tail(self):
        res = self.tail.prev
        self._remove(res) 
        return res
        

    def get(self, key: int) -> int:
        node = self.map.get(key, None)
        if not node:
            return -1
        self._move_to_front(node) 
        return node.value

        

    def put(self, key: int, value: int) -> None:

        node = self.map.get(key)
        if not node: 
            node = DLinkedNode() 
            node.key = key
            node.value = value
            self.map[key] = node
            self._insert(node)
            self.size +=1
            if self.size > self.capacity: 
                tail = self._remove_tail()
                del self.map[tail.key]
                self.size -= 1
        else:
            node.value = value 
            self._move_to_front(node)