
class Solution(object):
    def isPalindrome(self, x):
        #defines obj x as the input x
        self.x = x
        #list comprehension for int -> arr conversion
        x_arr = [x for x in str(self.x)]
        for i in range(0, int(len(x_arr)/1)):
            #if mirrored index position not the same cannot be palindrome
            #returns False
            if (x_arr[i] != x_arr[-(i + 1)]):
                return False
        #no false returns -> isPalindrome = True
        return True






