class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_to_close = {"(": ")", "{":"}", "[":"]"}

        for ch in s:
            if ch == "(" or ch == "{" or ch == "[":
                stack.append(ch)
            elif not stack or ch != open_to_close[stack.pop(-1)]:
                return False
        
        return not stack

        