class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #simplest case
        if len(s) != len(t):
            return False
        #def 2 blank hashes
        bookS, bookT = {}, {}
        #for each letter hash a tally
        for i in range(len(s)):
            bookS[s[i]] = bookS.get(s[i], 0) + 1
            bookT[t[i]] = bookT.get(t[i], 0) + 1
        #ret bool of if hashes are the same
        return bookS == bookT