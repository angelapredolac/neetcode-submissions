class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for s in strs:
            ret += str(len(s)) + "#" + s
        return ret

    def decode(self, s: str) -> List[str]:
        ind = 0
        ret = []
        
        while ind < len(s):
            j = ind

            while s[j]!="#":
                j+=1
            
            length = int(s[ind:j])

            start = j+1
            end = start+length

            ret.append(s[start:end])

            ind = end
        
        return ret
