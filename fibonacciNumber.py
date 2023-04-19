class Solution(object):
    def fib(self, n):
        #init var
        a, b, temp, end = 0, 1, None, None
        #if n < 2 ret n
        if n < 2: return n
        else:
            for i in range(n-1):
                end = a+b
                tmp = b
                b = end
                a = tmp
            #ret end point
            return end