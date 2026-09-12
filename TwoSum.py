class Solution(object):
    def twoSum(self, nums, target):
        seen={}
        for i,nums in enumerate(nums):
            needs=target-nums
            if needs in seen:
                return(seen[needs],i)
            seen[nums]=i
nums = [2,7,11,15]
target = 9
sol=Solution()
print(sol.twoSum(nums,target))
        