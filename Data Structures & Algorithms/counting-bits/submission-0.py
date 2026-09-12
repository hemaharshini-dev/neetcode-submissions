class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n + 1)

        for i in range(n + 1):
            x = i
            cnt = 0

            while x > 0:
                cnt += x & 1
                x >>= 1

            output[i] = cnt

        return output