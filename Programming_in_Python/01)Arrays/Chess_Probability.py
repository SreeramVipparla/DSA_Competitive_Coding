"""
QUESTION-

On an n x n chessboard, a knight starts at the cell (row, column) and attempts to make exactly k moves. The rows and columns are 0-indexed, so the top-left cell is (0, 0), and the bottom-right cell is (n - 1, n - 1).
A chess knight has eight possible moves it can make. Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.
Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.
The knight continues moving until it has made exactly k moves or has moved off the chessboard.
Return the probability that the knight remains on the board after it has stopped moving.

 
"""
"""
ANSWER-
"""
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(1, 2), (2, 1), (-1, 2), (-2, 1), (-1, -2), (-2, -1), (1, -2), (2, -1)]
        
        @lru_cache(None)
        def dfs(i, j, k):
            if k == 0:
                return 1
            count = 0
            for dx, dy in moves:
                x, y = i + dx, j + dy
                if x < 0 or x >= n or y < 0 or y >= n:
                    continue
                count += dfs(x, y, k -1)
            return count
        
        return dfs(row, column, k) / (8 ** k)
"""
SOURCE-LEETCODE
"""