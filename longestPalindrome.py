class Solution(object):
    def longestPalindrome(self, s):
        #len zero
        l = 0
        freq = {}
        #make dict of letter and freq
        for idx in s:
            freq[idx] = freq.get(idx, 0) + 1
        #if add up even values
        for f in freq.values():
            l += f // 2 * 2
        #if odd +1
        if any(x % 2 == 1 for x in freq.values()):
            l += 1
        return l