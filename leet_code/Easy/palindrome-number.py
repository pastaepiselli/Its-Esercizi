class Solution:
    def isPalindrome(self, x) -> bool:

        x = str(x)

        if len(x) <= 1:
            return True

        if x[0] != x[-1]:
            return False
        
        return self.isPalindrome(x[1:-1])
        
a = Solution()

print(a.isPalindrome(11))