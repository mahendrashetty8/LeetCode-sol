class Solution(object):
    def longestCommonPrefix(self, strs):
        
        p=strs[0]
        for word in strs[:1]:
            while not word.startswith(p):
                p=p[:-1]
            if p=="":
                return ""
strs = ["flower","flow","flight"]
sol=Solution()
print(sol.longestCommonPrefix(strs))
