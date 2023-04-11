class Solution(object):
    def pivotIndex(self, nums):
        left, right = 0, sum(nums)

        for i, num in enumerate(nums):
            right -= num

            if right == left:
                return i
            
            left += num

        return -1


            
sol = Solution()
print(sol.pivotIndex([2, 1, -1]))

# nums = [1,7,3,6,5,6]
# left = [x for x in nums]
# right = [y for y in nums]

# for i in range(1, len(nums)):
#     left[i] += left[i-1]
#     right[-i-1] += right[-i]

# for num in left:
#     if num in right and (right.index(num) - left.index(num) == 2):
#         print(left.index(num) + 1)
    
    



