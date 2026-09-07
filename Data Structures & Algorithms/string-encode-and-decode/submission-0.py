class Solution:

    def encode(self, strs: List[str]) -> str:
        e = ""
        for s in strs:
            e += str(len(s)) + '#' + s 
        return e
    def decode(self, s: str) -> List[str]:
        r = []
        i = 0
        while i<len(s):
            j = i
            while s[j]!='#':
                j+=1
            l = int(s[i:j])
            j+=1
            r.append(s[j:j+l])
            i = j+l
        return r

