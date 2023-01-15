class Solution:
    def grayCode(self, n: int):
        return (num ^ num>>1 for num in range(0,2**n))
