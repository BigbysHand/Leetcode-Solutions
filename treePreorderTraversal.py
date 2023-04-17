# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

def trav(root, arr):
    #traverses all branches and appends the root val to arr
    if root is None:
        return
    arr.append(root.val)
    for i in range(len(root.children)):
        trav(root.children[i], arr)

class Solution(object):
    #returns traversed pre ordered array
    def preorder(self, root):
        output = []
        trav(root, output)
        return output