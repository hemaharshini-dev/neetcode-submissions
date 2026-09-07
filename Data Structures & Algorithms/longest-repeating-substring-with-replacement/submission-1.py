class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        mf = 0
        l=0
        f = [0]*26
        for r in range(n):
            f[ord(s[r])-ord('A')]+=1
            mf = max(mf,f[ord(s[r])-ord('A')])
            while (r-l+1) - mf >k:
                f[ord(s[l])-ord('A')]-=1
                l+=1
                
            ans = max(ans,r-l+1)
        return ans
