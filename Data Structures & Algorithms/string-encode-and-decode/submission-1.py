class Solution:

    def encode(self, strs: List[str]) -> str:
        e = []
        for word in strs:
            e.append(str(len(word))+'#'+word )
        return "".join(e)


    def decode(self, s: str) -> List[str]:
        d = []
        i = 0
        while i<len(s):
            j = i
            while s[j]!='#':
                j+=1
            l = int(s[i:j])
            w = s[j+1:j+1+l]
            d.append(w)
            i = j+1+l
        return d

