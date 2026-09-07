class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        freq = {}
        for c1 in s:
            freq[c1] = freq.get(c1,0)+1
        for c1 in t:
            if c1 not in freq:
                return False
            freq[c1]-=1 
            if freq[c1] < 0:
                return False 
        return True