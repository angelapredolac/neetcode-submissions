class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        left = 0 
        max_freq = 0
        longest = 0

        for right in range(len(s)):
            char = s[right]
            counts[char] = counts.get(char, 0) + 1

            max_freq = max(max_freq, counts[char])

            while (right-left+1) - max_freq > k:
                counts[s[left]] -= 1
                left += 1
            
            longest = max(longest, right-left+1)

        return longest


"""
s = "XYYX", k = 2
keep track of counts during sliding window 
"""