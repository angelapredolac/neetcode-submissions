class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        cleaned_s = ''.join([char for char in s if char.isalnum()])
        return cleaned_s==cleaned_s[::-1]
        