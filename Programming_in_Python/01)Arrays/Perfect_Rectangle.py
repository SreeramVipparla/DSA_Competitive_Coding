"""
QUESTION-
Given an array rectangles where rectangles[i] = [xi, yi, ai, bi] represents an axis-aligned rectangle. The bottom-left point of the rectangle is (xi, yi) and the top-right point of it is (ai, bi).

Return true if all the rectangles together form an exact cover of a rectangular region.

 

Example 1:


Input: rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
Output: true
Explanation: All 5 rectangles together form an exact cover of a rectangular region.
Example 2:


Input: rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]
Output: false
Explanation: Because there is a gap between the two rectangular regions.
Example 3:


Input: rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]
Output: false
Explanation: Because two of the rectangles overlap with each other.
 

Constraints:

1 <= rectangles.length <= 2 * 104
rectangles[i].length == 4
-105 <= xi, yi, ai, bi <= 105
"""
"""
ANSWER-
"""
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        area = 0
        corner = set()
        X0 = Y0 = inf
        X1 = Y1 = -inf
        for x0, y0, x1, y1 in rectangles: 
            area += (x1-x0)*(y1-y0)
            X0 = min(x0, X0)
            Y0 = min(y0, Y0)
            X1 = max(x1, X1)
            Y1 = max(y1, Y1)
            corner ^= {(x0, y0), (x0, y1), (x1, y0), (x1, y1)}
        return area == (X1-X0)*(Y1-Y0) and corner == {(X0, Y0), (X0, Y1), (X1, Y0), (X1, Y1)}
"""
SOURCE-LEETCODE
"""


