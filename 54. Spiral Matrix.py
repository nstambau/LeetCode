//  https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, A: List[List[int]]) -> List[int]:
        
        import numpy as np
        A = np.asarray(A)
        out = []
    
        for ii in range(0,len(A)+len(A[0])):
            if len(A) == 0 or len(A[0]) == 0:
                continue
            if ii%4 == 0: #top
                out.append(A[0,:])
                A = np.delete(A,0,0)
            elif ii%4 == 1: #right
                out.append(A[:,-1])
                A = np.delete(A,-1,1)
            elif ii%4 == 2: #bottom
                out.append(np.flip(A[-1,:]))
                A = np.delete(A,-1,0)
            elif ii%4 == 3: #left
                out.append(np.flip(A[:,0]))
                A = np.delete(A,0,1)
        
        return np.concatenate(out)
