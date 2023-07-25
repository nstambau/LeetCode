## https://leetcode.com/problems/maximum-star-sum-of-a-graph

class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:

      # Given a list of (positive values from adjacent verticies, return sum of largest m
        def sum_k_largest(num_list, m):
            listPos = [x for x in num_list if x > 0]
            if len(listPos) == 0 or m==0:
                return 0
            elif len(listPos) <= m:
                return sum(listPos)
            else:
                listSorted = sorted(listPos)
                return sum(listSorted[-m:])

      # initialize
        out = -10**4

      # Trivial case
        if len(vals)==1:
            return vals[0]

      # Run through the list of edges and build an array of verticies in each star
        adjVerticies = [[] for ii in range(0,len(vals))]
        for edge in edges:
            adjVerticies[edge[0]].append(edge[1])
            adjVerticies[edge[1]].append(edge[0])

      # Now loop through each vertex as a center, and add it's value to those around it
        for center in range(0,len(vals)):
            adjVal = [vals[adj] for adj in adjVerticies[center]]
            best = vals[center]+sum_k_largest(adjVal,k)
            ##print([adjVal,":  ",best])
            if best > out:
                out = best

        return out
