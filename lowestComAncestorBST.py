# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#finds the node where p and q lie either side
def rootFinder(root, p, q):
    if (p.val < root.val) and (q.val < root.val):
        return rootFinder(root.left, p, q)
    elif (p.val > root.val) and (q.val > root.val):
        return rootFinder(root.right, p, q)
    else:
        return root

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        #start recurssion
        return rootFinder(root, p, q)