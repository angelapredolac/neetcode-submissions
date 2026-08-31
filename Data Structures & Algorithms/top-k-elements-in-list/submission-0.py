class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elems_to_counts = {}
        for num in nums:
            if num not in elems_to_counts.keys():
                elems_to_counts[num]=1
            else:
                elems_to_counts[num]+=1
        counts = []
        for key in elems_to_counts.keys():
            counts.append([key, elems_to_counts[key]])
        counts = sorted(counts, key=lambda x: x[1], reverse=True)
        return [x for x, _ in counts[0:k]]
        