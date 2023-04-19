class Solution(object):
    def climbStairs(self, n):
        m = n + 1
        #init var
        a, b, temp, end = 0, 1, None, None
        #if n < 2 ret n
        if m < 2: return m
        else:
            for i in range(m):
                end = a+b
                tmp = b
                b = end
                a = tmp
            #ret end point
            return end