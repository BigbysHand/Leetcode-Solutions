class Solution(object):
    def pivotIndex(self, nums):
        #init left to 0 and right to tot
        left, right = 0, sum(nums)
        #sub right, add left
        for i, num in enumerate(nums):
            right -= num
            #buble gap of one index to check here for piv
            if right == left:
                #ret index if buble index is pivot
                return i
            #add to left
            left += num
        #no pivot
        return -1




