class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if not s or not t:
            return ""
        
        counts_t = {}
        for ch in t:
            counts_t[ch] = counts_t.get(ch, 0) + 1
        
        window_counts = {}

        required = len(counts_t)
        formed = 0

        start = 0
        best_start = 0
        best_length = float("inf")

        for end in range(len(s)):
            # expand the window by adding s[end]
            right_char = s[end]
            window_counts[right_char] =  window_counts.get(right_char, 0) + 1

            # this character has reached its required frequency
            if (
                right_char in counts_t
                and window_counts[right_char] == counts_t[right_char]
            ):
                formed += 1
            
            # shrink the window while it still contains all of t
            while formed==required:
                window_length = end-start+1

                if window_length < best_length:
                    best_length = window_length
                    best_start = start
                
                left_char = s[start]
                window_counts[left_char] -= 1

                # removing this character makes the window invalid
                if (
                    left_char in counts_t
                    and window_counts[left_char] < counts_t[left_char]
                ):
                    formed -= 1
                
                start += 1
 
        if best_length == float('inf'):
            return ""
        
        return s[best_start:best_start+best_length]

            


"""
OUZODYXAZV
ZODYX
YXAZ

"""
        
                
        