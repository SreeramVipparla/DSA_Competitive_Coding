"""
QUESTION-

Given the head of a linked list, rotate the list to the right by k places.
Eg:-
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3] 
"""
"""
ANSWER-
"""
class Solution(object):
    def rotateRight(self, head, k):        
        if not head:
            return head

        length = 1
        tail = head
        
        while tail.next:
            tail = tail.next
            length += 1
        
        k %= length
        
        if k == 0:
            return head
        

        steps_to_new_head = length - k
        tail.next = head
        
        while steps_to_new_head > 0:
            tail = tail.next
            steps_to_new_head -= 1

        new_head = tail.next
        tail.next = None
        
        return new_head
"""
SOURCE-LEETCODE
"""