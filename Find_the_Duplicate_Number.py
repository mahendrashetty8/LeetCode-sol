class Solution(object):
    def findDuplicate(self, nums):
        fre = set()

        for i in nums:
            if i in fre:
                return i
            fre.add(i)

nums = [1,3,4,2,2]
sol=Solution()
print(sol.findDuplicate(nums))
        