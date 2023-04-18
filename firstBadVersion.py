# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    if version == 4: return True
    else: return False

class Solution(object):
    def firstBadVersion(self, n):
        #left and right init to 1 and n
        L = 1
        R = n
        #while L < R
        while L < R:
            m = (L+R)//2
            #if mid is bad, bad on lhs inclusive
            if isBadVersion(m):
                R = m
            #else rhs exclusive
            else:
                L = m + 1
        #L will converge to the first bad
        return L

            
                                 

