class Solution(object):
    def isIsomorphic(self, s, t):
        #gen zipped list
        linked = list(zip(s, t))
        #if length of reduced linked list not same are reduced s or t then false
        if (len(set(linked)) != len(set(s)) or (len(set(linked)) != len(set(t)))):
            return False
        #is true if no fails
        return True
            