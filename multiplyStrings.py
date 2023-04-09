class Solution(object):
    def multiply(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

        #converting ins to ints
        num1 = int(num1)
        num2 = int(num2)

        #mult
        output = str(num1 * num2)
        
        return output
        