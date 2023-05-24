"""
implement an LRU cache. 

classic interview problem - should be able to explain how/why it works and also be able to explain the reasoning behind the data structure. 

"""

# we need to use a doubly linked list with pointers to nodes stored in a hashmap. 
# every time a node gets accessed we need to move that node to the head. Because of this reason, 
# doubly linked lists are fit as they make easy additions to the head.
# doubly linked lists have an inherent problem of linked lists in that they amortize to a linear time on search O(n) 
# we reduce this by storing such pointer to a hashmap. 
# by doing this, we achieve both O(1) retrieval as well as O(1) insert. 


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
    
lrucache = LRUCache(2)
lrucache.put(1, 1) # // cache is {1=1}
lrucache.put(2, 2) # // cache is {1=1, 2=2}
lrucache.get(1)    # // return 1
lrucache.put(3, 3) # // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lrucache.get(2)    # // returns -1 (not found)
lrucache.put(4, 4) #  LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lrucache.get(1)    # return -1 (not found)
lrucache.get(3)    # return 3
lrucache.get(4)    # return 4