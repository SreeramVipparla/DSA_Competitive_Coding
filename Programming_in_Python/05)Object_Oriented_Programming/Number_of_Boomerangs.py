"""
QUESTION-
You are given n points in the plane that are all distinct, where points[i] = [xi, yi]. A boomerang is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Return the number of boomerangs.

 

Example 1:
Input: points = [[0,0],[1,0],[2,0]]
Output: 2
Explanation: The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]].

Example 2:
Input: points = [[1,1],[2,2],[3,3]]
Output: 2

Example 3:
Input: points = [[1,1]]
Output: 0
 

Constraints:

n == points.length
1 <= n <= 500
points[i].length == 2
-104 <= xi, yi <= 104
All the points are unique.


"""
"""
ANSWER-
"""
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return 0
        
        res = 0
       
        for p1 in points:
            tmp = {}
            for p2 in points:
                d = self.dist(p1, p2)
                tmp[d] = tmp.get(d, 0) + 1
            for val in [val for val in tmp.values() if val > 1]:
                res += val * (val - 1)
                
        return res
        
    def dist(self, p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
"""
SOURCE-LEETCODE
"""