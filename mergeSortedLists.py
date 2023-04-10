#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        #init head & currentNode
        head = ListNode()
        currentNode = head
        #check for first merging condition while iterating through linked list
        while(list2 != None and list1 != None):
            if list1.val < list2.val:
                currentNode.next = list1
                list1 = list1.next
            else:
                currentNode.next = list2
                list2 = list2.next
            currentNode = currentNode.next
        #adds the list nodes to the result
        if list1 != None:
            currentNode.next = list1
        if list2 != None:
            currentNode.next = list2
        #returns the head of the returned linked list
        return head.next



