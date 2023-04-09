# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head = ListNode()
        currentNode = head  
        carry = 0

        while(l1 != None or l2 != None or carry != 0):
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0

            sum = l1val + l2val + carry

            currentNode.next = ListNode(sum % 10)
            carry = sum // 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            currentNode = currentNode.next

        return head.next

a = [9,9,9,9,9,9,9]
b = [9, 9, 9, 9]

l1 = ListNode()
l2 = ListNode()

for i, elements in enumerate(a):
    l1.next = ListNode(elements)
    l1 = l1.next
for i, elements in enumerate(b):
    l2.next = ListNode(elements)
    l2 = l2.next

while l1 != None:
    print(l1.val)
    l1 = l1.next

sol = Solution()

print(sol.addTwoNumbers(l1, l2).next)
