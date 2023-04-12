class Solution(object):
    def reverse(self, x):
        #final mult
        mult = 1
        #if les than one make pos and mult is -1
        if x < 0:
            mult = -1
            x *= -1
        #makes into mutable array
        x_arr = [i for i in str(x)]
        x_out = mult*int("".join(x_arr[::-1])) 
        #if rev int in bounds
        if x_out < 2**31 - 1 or x_out > -2**31:
            return x_out
        #out of bounds
        return 0