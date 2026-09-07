class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ml = 0
        l=0
        setc = set()
        for r in range(len(s)):
            while s[r] in setc:
                setc.remove(s[l])
                l+=1
            setc.add(s[r])
            ml = max(ml,r-l+1)
        return ml
