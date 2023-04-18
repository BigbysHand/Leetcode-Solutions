class Solution(object):
    def mergeAlternately(self, word1, word2):
        #merge str
        merge = ""
        i = 0
        #while words not at limit add words one after the other
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                merge += word1[i]
            if i < len(word2):
                merge += word2[i]
            i+=1
        #ret merged
        return merge
        

        