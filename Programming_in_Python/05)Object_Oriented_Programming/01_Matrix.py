"""
QUESTION-
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
"""
"""
ANSWER-
"""
class Solution:
	def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
		Row, Col = len(mat), len(mat[0])
		queue = []
		directions = [[0, +1], [0, -1], [1, 0], [-1, 0]]

		for i in range(Row):
			for j in range(Col):
				if mat[i][j] == 0:
					queue.append((i, j)) 
				else:
					mat[i][j] = "*"

		for r, c in queue:
			for dr, dc in directions:
				row = r + dr
				col = c + dc
				if 0 <= row < Row and 0 <= col < Col and mat[row][col] == "*":
					mat[row][col] = mat[r][c] + 1
					queue.append((row, col))
		return mat
"""
SOURCE-LEETCODE
"""