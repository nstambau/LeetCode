##  https://leetcode.com/problems/gray-code
##  Memory Use beats 70.16% of users with Python3

class Solution:
    def grayCode(self, n: int) -> List[int]:

        def buildMat(A,k,n):
            if k==n:
                return A
            B = [A[-ii]+2**k for ii in range(1,1+2**k)]
            return buildMat(A+B,k+1,n)

        return buildMat([0,1],1,n)
