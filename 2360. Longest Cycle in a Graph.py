## https://leetcode.com/problems/longest-cycle-in-a-graph
## Runtime beats 89.04% of users with Python3
## Memory beats 98.23% of users with Python3

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        cyc = -1
        for ii in range(0,len(edges)):
            if edges[ii]<0:
                continue
            start = [ii]
            go = True

            while go:
                if edges[start[-1]]<0:
                    go = False
                else:
                    start.append(edges[start[-1]])
                    edges[start[-2]] = -1
            if start[-1] in start[:-1]:
                cyc = max(cyc,len(start)-1-start.index(start[-1]))
        return cyc
