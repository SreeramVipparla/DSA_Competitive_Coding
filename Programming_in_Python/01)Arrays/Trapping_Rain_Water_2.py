"""
QUESTION-
Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.

 

Example 1:


Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
Output: 4
Explanation: After the rain, water is trapped between the blocks.
We have two small ponds 1 and 3 units trapped.
The total volume of water trapped is 4.
Example 2:


Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
Output: 10
 

Constraints:

m == heightMap.length
n == heightMap[i].length
1 <= m, n <= 200
0 <= heightMap[i][j] <= 2 * 104
"""
"""
ANSWER-
"""

from collections import defaultdict
import heapq
class Solution:
    Inf = float('inf')
    def didj(self,i,j):
        r,c = self.r,self.c
        for a,b in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
            if 0<=a<r and 0<=b<c:
                yield a,b
    def trapRainWater(self, A):
        if not A:
            return 0
        r,c = self.r,self.c = len(A), len(A[0])
        if r<=2 and c<=2:
            return 0
        #
        Inf   = self.Inf
        water = defaultdict( lambda: Inf )
        #
        leakage = set()
        leakage.update({ ( i   ,   0) for i in range(r) })
        leakage.update({ ( i   , c-1) for i in range(r) })
        leakage.update({ (   0 ,   j) for j in range(c) })
        leakage.update({ ( r-1 ,   j) for j in range(c) })
        #
        genkey = lambda i,j: ( A[i][j],i,j )
        stack = [ genkey(i,j) for i,j in leakage ]
        heapq.heapify(stack)
        #
        self.res = 0
        def dfs(i,j,lvl):
            if (i,j) in leakage:
                return
            Aij, wij = A[i][j], water[i,j]
            if lvl>Aij:
                # Lake Encountered
                if lvl<wij:
                    # New Leakage Detected
                    # -> Compute Old Water Held
                    old        = 0 if (wij == Inf) else wij - Aij
                    # -> Update Water Storage
                    self.res  += lvl - Aij - old
                    water[i,j] = lvl
                    # -> Propagate Water Leakage
                    for a,b in self.didj(i,j):
                        dfs(a,b,lvl)
            else:
                # Tower found (this may be a source of leaks in the future)
                leakage.add   ( (i,j) )
                heapq.heappush( stack, genkey(i,j) )
                if wij<Inf:
                    self.res  -= wij - Aij
        while stack:
            lvl,i,j = heapq.heappop(stack)
            for a,b in self.didj(i,j):
                dfs(a,b,lvl)
        #
        return self.res

"""
SOURCE-LEETCODE
"""