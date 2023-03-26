class Solution(object):
    def romanToInt(self, s):
        self.s = s

        #string to arr conv
        string = list(self.s)
        
        #conv roman num tally
        conv = 0

        #could define as tuple, but not really worth it in this case
        sym = ["I", "V", "X", "L", "C", "D", "M"]
        num = [1, 5, 10, 50, 100, 500, 1000]

        #checking for the specific case and systematically removing them
        for i in range(0, len(string) - 1):
            selector = s[i] + s[i+1]
            
            if selector == "IV":
                conv += 4
                string.remove("I")
                string.remove("V")


            elif selector == "IX":
                conv += 9
                string.remove("I")
                string.remove("X")

            elif selector == "XL":
                conv += 40
                string.remove("X")
                string.remove("L")

            elif selector == "XC":
                conv += 90
                string.remove("X")
                string.remove("C")

            elif selector == "CD":
                conv += 400
                string.remove("C")
                string.remove("D")
            
            elif selector == "CM":
                conv += 900
                string.remove("C")
                string.remove("M")
            
        #tallyying final array
        for syms in string:
            index = sym.index(syms)
            conv += num[index]

        return conv
    