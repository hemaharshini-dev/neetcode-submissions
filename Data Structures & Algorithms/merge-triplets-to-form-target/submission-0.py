class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target

        a = b = c = False

        for i, j, k in triplets:
        
            if i > x or j > y or k > z:
                continue

        
            if i == x:
                a = True
            if j == y:
                b = True
            if k == z:
                c = True

        return a and b and c