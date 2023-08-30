class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        #def blank hash
        prevDiff = {}
        for i, x in enumerate(nums):
            #diff is target - curr number
            diff = target - x
            if diff in prevDiff:
                #ret since if diff already in hash then diff index and current are two sum
                return [prevDiff[diff], i]
            #let hash -> number:index
            prevDiff[x] = i