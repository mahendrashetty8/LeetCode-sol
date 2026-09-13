class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        original = x
        reversed_x = 0
        while x > 0:
            reversed_x = reversed_x * 10 + x % 10
            x //= 10
        return reversed_x == original

sol = Solution()
x = 121
print(sol.isPalindrome(x))