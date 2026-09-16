class Solution(object):
    def removeElement(self, nums, val):
        
        while val in nums:
            nums.remove(val)
        for i in range(len(nums)):
            nums[i]=nums[i]
        return len(nums)
s=Solution()
nums = [3,2,2,3]
print(s.removeElement(nums,3))