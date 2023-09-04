class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        #define arr of ones 
        res = [1] * len(nums)
        #prefix products start at 1
        prefix = 1
        #iter: res[i] = prefix, update prexif to product tally
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        #init suffix = 1
        suffix = 1
        #iter: res[i] *= suffix, update suffix to backwards product tally
        for i in range(len(nums)-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res


        