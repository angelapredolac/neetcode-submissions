class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_to_words = {}
        for str in strs:
            sorted_str = "".join(sorted(str))
            if sorted_str not in sorted_to_words:
                sorted_to_words[sorted_str] = []
            sorted_to_words[sorted_str].append(str)
        return [val for val in sorted_to_words.values()]
        