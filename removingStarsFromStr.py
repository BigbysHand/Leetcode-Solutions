class Solution(object):
    def removeStars(self, s):
        output = []
        for i in range(len(s)):
            if s[i] == "*":
                output.pop()
            else:
                output += s[i]
        return "".join(output)
    

sol = Solution()

print(sol.removeStars("leet**cod*e"))