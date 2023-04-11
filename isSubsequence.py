class Solution(object):
    def isSubsequence(self, s, t):
        #position set to 0
        pos = 0
        #for elements in s
        for ele in s:
            #positions is set to the pos of ele in t starting from init pos
            #+1 to pos to make it the next pos 
            pos = t.find(ele, pos) + 1
            #if find returns -1 pos = 0 -> ret false
            if pos == 0:
                return False
        #no fails -> ret true
        return True