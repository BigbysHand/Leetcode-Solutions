from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        #def dict of params list
        out = defaultdict(list)
        for word in strs:
            #def count key as 26 zerod array
            count = [0] * 26 
            for letter in word:
                #conv letter to nums at index and inc if valid
                count[ord(letter) - ord("a")] += 1
            #append the word at key count to dict
            out[tuple(count)].append(word)
        #return values of dict
        return out.values()