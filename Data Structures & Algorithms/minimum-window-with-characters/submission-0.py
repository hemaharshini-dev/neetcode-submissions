class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        have = 0
        w = {}
        nc = len(need)
        l = 0
        ml = float('inf')
        ans=""
        for r in range(len(s)):
            c = s[r]
            w[c] = w.get(c,0)+1
            if c in need and w[c]==need[c]:
                have+=1
            while have == nc:
                if r-l+1<ml:
                    ml = r-l+1
                    ans = s[l:r+1]
                lc = s[l]
                w[lc]-=1
                if lc in need and w[lc]<need[lc]:
                    have-=1 
                l+=1 
        return ans