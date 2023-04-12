# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        #init prev as None, cur as head
        prev = None
        cur = head
        #while cur not None
        while cur != None:
              #point temp to the next node in head
              tmp = cur.next
              #next node points to prev (1st case None)
              #so 1st node linked to None
              cur.next = prev
              #prev node set to cur
              prev = cur
              #current shifted to next node in head
              cur = tmp
        #return prev as will be set to start of new linked list
        return prev






