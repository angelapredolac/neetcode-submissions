from itertools import combinations

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        user_visits = {}
        for i in range(len(username)):
            user = username[i]
            time = timestamp[i]
            webpage = website[i]
            if user not in user_visits:
                user_visits[user] = []
            user_visits[user].append((time, webpage))

        pattern_counts = {}
        for user, visits in user_visits.items():
            # sort visits chronologically for each user 
            visits.sort()
            webpages = [visit[1] for visit in visits]
            patterns = set(combinations(webpages, 3))
            
            for pattern in patterns:
                if pattern not in pattern_counts:
                    pattern_counts[pattern]=0
                pattern_counts[pattern]+= 1
        
        most_freq_pattern = None
        max_count =0

        # find the pattern with the highest freq,
        # or the smallest pattern if there are ties 
        for pattern, count in pattern_counts.items():
            if count > max_count:
                max_count = count 
                most_freq_pattern = pattern
            elif count == max_count:
                if pattern < most_freq_pattern:
                    most_freq_pattern = pattern
        
        return list(most_freq_pattern)




"""
step 1: build dict username: websites in order

step 2: build array of all patterns, lexicographically sorted 

step 3: compute score of each pattern

step 4: return max pattern
"""
        