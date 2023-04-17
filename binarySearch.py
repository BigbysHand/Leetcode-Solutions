class Solution(object):
    def search(self, nums, target):
        l = len(nums)
        #start and end points init
        L = 0
        R = l-1
        #shifting mid point around till mid is target (binary search)
        while L <= R:
            mid = (R + L) // 2
            if nums[mid] < target:
                L = mid + 1
            elif nums[mid] > target:
                R = mid - 1
            else:
                return mid
        return -1            