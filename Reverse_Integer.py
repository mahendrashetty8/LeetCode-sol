class Solution(object):
    def reverse(self, x):
        if x<0:
            sig=-1 
        else:
            sig=1
        x=abs(x)
        rev=0
        while x>0:
            num=x%10
            rev=rev*10+num
            x//=10
        rev=rev*sig

        if rev<-2**32 or rev>2**32 -1:
            return 0
        return rev

sol=Solution()
x=1230
sol.reverse(x)
