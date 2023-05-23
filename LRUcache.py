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

class LRU: 
    class DLLNode: 
        def __init__(self, val) -> None:
            self.val = val 
            self.prev = None
            self.next = None 

    def __init__(self) -> None:
        self.capacity = 4
        self.head = self.DLLNode(None)
        self.tail = self.DLLNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}
    

    # new node into the front of the queue
    def _insert(self, val): 
        newNode = self.DLLNode(val) 
        newNode.next = self.head.next
        self.head.next = newNode
        if self.tail.prev == self.head: 
            self.tail.prev = newNode
        if not newNode in self.map:
            self.map[newNode] = 1

    def _delete(self, node): 
        if self.head.next == self.tail:
            # linkedlist is empty
    
