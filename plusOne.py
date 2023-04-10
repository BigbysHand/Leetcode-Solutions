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
        #adds one to the integer
        asNum += 1
        #convert back to array
        result = [int(x) for x in str(asNum)]
        #returns the result
        return result
    
