class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        b = [[] for _ in range(len(nums)+1)]
        for num,freq in count.items():
            b[freq].append(num)
        r =[]
        for f in range(len(b)-1,0,-1):
            for n in b[f]:
                r.append(n)
                if len(r)==k:
                    return r

