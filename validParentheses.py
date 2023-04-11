class Solution(object):
    def isValid(self, s):
        #gen stack
        stack = []
        #runs through string
        for bra in s:
            #if opening
            if bra in "([{":
                #add to stack
                stack.append(bra)
            #if close
            else:
                #if stack empty or close has no proper closer
                if not stack or \
                (bra == ")" and stack[-1] != "(") or \
                (bra == "]" and stack[-1] != "[") or \
                (bra == "}" and stack[-1] != "{"):
                    #return false
                    return False
                #handled so pop
                stack.pop()
        #if all stack empty after checks then not stack == True
        return not stack
