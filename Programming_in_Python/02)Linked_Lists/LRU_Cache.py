"""
QUESTION-

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.
Eg:-
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

"""
"""
ANSWER-
"""
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.dic = dict() # key to node
        self.capacity = capacity
        self.head = ListNode(0, 0)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:             # similar to get()        
            node = self.dic[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            node.value = value         # replace the value len(dic)
        else: 
            if len(self.dic) >= self.capacity:
                self.removeFromTail()
            node = ListNode(key,value)
            self.dic[key] = node
            self.insertIntoHead(node)
			
    def removeFromList(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insertIntoHead(self, node):
        headNext = self.head.next 
        self.head.next = node 
        node.prev = self.head 
        node.next = headNext 
        headNext.prev = node
    
    def removeFromTail(self):
        if len(self.dic) == 0: return
        tail_node = self.tail.prev
        del self.dic[tail_node.key]
        self.removeFromList(tail_node)
"""
SOURCE-LEETCODE
"""