# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        #base case
        if root is None:
            return
        #ret arr
        order = []
        #queue
        q = []
        #to start add the root to the queue
        q.append(root)
        #while q is filled
        while q:
            #length of q and store init
            l = len(q)
            store = []
            #for nodes in q
            for i in range(l):
                #node = poped 0th q
                node = q.pop(0)
                #q instance values appended
                store.append(node.val)
                #adds the next values to the queve
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            #store appended to order
            order.append(store)
        #ret order   
        return order



