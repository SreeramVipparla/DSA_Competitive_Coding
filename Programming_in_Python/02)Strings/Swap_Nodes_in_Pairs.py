"""
QUESTION-

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Eg:-
Input: head = [1,2,3,4]
Output: [2,1,4,3]
"""
"""
ANSWER-
"""
def recursive(self, head):
        def rec(head):
            if head and head.next:
                rep = rec(head.next.next)
                second = head.next
                first = head
                if second:
                    first.next = rep
                    second.next = first
                    return second
                return first
            elif head: return head
            
        return rec(head)
    
    def in_place_nodes(self, head):
        if not head: return head
        prev = None
        first = head
        second = head.next
        while first and second:
            if prev:
                prev.next = second
            else:
                head = second
            forward = second.next
            first.next = second.next
            second.next = first
            prev = first
            first = forward
            if not first: break
            second = first.next
        return head
    
        
    def in_place_value(self, head):
        if not head: return head
        first = head
        second = head.next
        while first and second:
            first.val, second.val = second.val, first.val
            first = second.next
            if not first: break
            second = second.next.next
        return head
"""
SOURCE-LEETCODE
"""