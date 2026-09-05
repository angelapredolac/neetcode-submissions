class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        l = 0
        s1 = sorted(s1)
        for right in range(l+len(s1)-1, len(s2)):
            if s1 == sorted(s2[right-len(s1)+1:right+1]):
                return True
        return False
