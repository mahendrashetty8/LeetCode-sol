class Solution(object):
    def removeDuplicates(self, nums):
        fre =[] 
        for i in nums:
            if i not in fre:
                fre.append(i)
        for i in range(len(fre)):
            nums[i]=fre[i]
        return len(fre)