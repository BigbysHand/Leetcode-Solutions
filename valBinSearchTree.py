# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def valid(root, min, max):
    if root is None:
        return True
    if not (min < root.val and root.val < max):
        return False
    return valid(root.left, min, root.val) and \
        valid(root.right, root.val, max)

class Solution(object):
    def isValidBST(self, root):
        return valid(root, (-20000000000), (20000000000))