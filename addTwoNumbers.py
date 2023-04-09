class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # self.l1 = l1
        # self.l2 = l2

        #ints from arrays (reversed)
        l1num = sum(num * 10**i for i, num in enumerate(l1[::-1]))
        l2num = sum(num * 10**i for i, num in enumerate(l2[::-1]))

        summing = l1num + l2num

        #making back into array
        output = [int(x) for x in str(summing)[::-1]]

        return output


        
sol = Solution()

print(sol.addTwoNumbers([9,9,9,9,9,9,9], [9, 9, 9, 9]))
