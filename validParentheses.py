class Solution(object):
    def isValid(self, s):
        stack = []

        for bra in s:
            if bra in "([{":
                stack.append(bra)
            else:
                if not stack or \
                (bra == ")" and stack[-1] != "(") or \
                (bra == "]" and stack[-1] != "[") or \
                (bra == "}" and stack[-1] != "{"):
                    return False
                stack.pop()
        return not stack


sol = Solution()

print(sol.isValid("{[]}"))

# s = "[{()}]"
# a = [1, 5, 2, 6, 2]

# for i in range((len(s) + 1) // 2):
#     if s[i] == s[-1-i]:
#         #print(s)
#         s.replace(s[i], "")
        
# print(a[-1])
