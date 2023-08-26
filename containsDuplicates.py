class Solution(object):
    def containsDuplicate(self, nums):
        #init empty hash
        catch = set()
        #iter through nums
        for x in nums:
            #if x in hash ret true
            if x in catch:
                return True
            #add num to hash
            catch.add(x)
        return False