class Solution(object):
    def removeStars(self, s):
        #out arr
        output = []
        #for char in s
        for i in s:
            #if i is a star pop last append
            if i == "*":
                output.pop()
            #else app i
            else:
                output.append(i)
        #ret str of output
        return "".join(output)