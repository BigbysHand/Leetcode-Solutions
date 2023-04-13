class Solution(object):
    def removeDuplicates(self, nums):
        #in place method
        nums[:] = sorted(set(nums))
        return len(nums)
