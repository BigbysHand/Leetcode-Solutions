class Solution(object):
    def strStr(self, haystack, needle):
        #python voodoo magic
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1