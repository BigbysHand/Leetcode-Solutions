class Solution(object):
    def plusOne(self, digits):
        self.digits = digits

        #define logic variables and arrays
        asNum = 0 
        length = len(self.digits)
        result = []

        #converts the array into a number
        for i, num in enumerate(self.digits):
            try:
                asNum += 10**(length - i - 1) * num
            except ValueError:
                print("array contains wrong values")

        asNum += 1

        result = [int(x) for x in str(asNum)]

        return result
    

sol = Solution()

print(sol.plusOne([9, 8, 9, 1, 9]))