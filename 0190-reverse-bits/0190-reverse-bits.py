class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            
            if n >> 1 << 1 != n:
                n = n >> 1
                res += pow(2,31-i)
            else:
                n = n >> 1
        return res
            