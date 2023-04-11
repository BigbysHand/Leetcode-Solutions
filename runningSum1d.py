class Solution(object):
    def runningSum(self, nums):
        #init 1st pos
        runSum = [nums[0]]
        #append sum of num in nums with prev runSum index
        for i, num in enumerate(nums[1:]):
            runSum.append(num + runSum[i])
        #return runSum
        return runSum

