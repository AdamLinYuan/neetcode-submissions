class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s)).lower()
        for i in range(0, len(s)//2):
            print(s[i], s[-i-1])
            if s[i] != s[-i-1]:
                return False

        return True