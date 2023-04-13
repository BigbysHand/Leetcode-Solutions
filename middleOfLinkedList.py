# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def middleNode(self, head):
        #length is zero
        length = 0
        #cur points to head node
        cur = head
        #iter through head for length
        while head:
            length += 1
            head = head.next
        #find mid point iter to mid node
        for i in range(length//2):
            cur = cur.next
        #ret node
        return cur