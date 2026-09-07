class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for word in strs:
            a = [0]*26
            for ch in word:
                a[ord(ch)-ord('a')]+=1
            key = tuple(a)
            group.setdefault(key,[]).append(word)
        return list(group.values())
            