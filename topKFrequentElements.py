class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        #hash tally
        tally = {}
        #arr for inv tally
        invBucket = [[] for i in range(len(nums) + 1)]
        #hash counter
        for i in range(len(nums)):
            tally[nums[i]] = 1 + tally.get(nums[i], 0)
        #for tuples in items of tally
        for (i, c) in tally.items():
            #appends the value ot array index of tally amount
            invBucket[c].append(i)
        freq = []
        #iter reverse through inv tally
        for i in range(len(invBucket) - 1, 0, -1):
            #for elements in each freq index
            for n in invBucket[i]:
                freq.append(n)
                #if lenghth of k freq == k ret freq
                if len(freq) == k:
                    return freq