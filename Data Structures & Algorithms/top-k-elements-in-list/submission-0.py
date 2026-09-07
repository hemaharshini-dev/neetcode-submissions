from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        r = []
        for _ in range(k):
            mn = None
            mf = 0
            for i in count:
                if count[i] >mf:
                    mf = count[i]
                    mn = i
            r.append(mn)
            del count[mn]
        return r


        