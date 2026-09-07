class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        c1 = Counter(s1)
        for i in range(m-n+1):
            w = s2[i:i+n]
            if Counter(w)==c1:
                return True 
        return False

