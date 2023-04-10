# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        #init 
        head = ListNode()
        currentNode = head  
        carry = 0

        #while both linkedLists in range and carry is not zero
        while(l1 != None or l2 != None or carry != 0):
            #appropriate value set 
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0

            #sum
            sum = l1val + l2val + carry

            #next node set to mod of 
            currentNode.next = ListNode(sum % 10)
            #floor div of 10 for carry = 0 or 1
            carry = sum // 10

            #mving along linked list
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            currentNode = currentNode.next
        #returns the head position of the first node
        return head.next


