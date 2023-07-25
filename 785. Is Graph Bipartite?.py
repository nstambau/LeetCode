##  https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        ell = set(i for j in graph for i in j)
        if len(ell)==0:
            return True
        n = max(ell)

        import numpy as np

        adj = np.zeros((n+1,n+1))
        for ii in range(0,len(graph)):
            for jj in graph[ii]:
                adj[ii][jj] =1
                adj[jj][ii] =1

        return sum(abs(np.diagonal(np.linalg.matrix_power(adj,2*n+1)))) == 0
