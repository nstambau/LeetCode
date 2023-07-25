## https://leetcode.com/problems/where-will-the-ball-fall/


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        import numpy as np
        loc = np.asarray(list(range(0,len(grid[0]))))
        if len(grid[0])==1:
            return [-1]
        n = len(grid[0])
        for row in grid:
            row = np.asarray([1]+row+[-1])
            mask = (row[1:-1]>=row[:-2])*(row[2:]>=row[1:-1])
            for ball in range(0,n):
                if loc[ball]<0:
                    continue
                loc[ball] = loc[ball] + row[loc[ball]+1] if mask[loc[ball]] else -1
        return loc
