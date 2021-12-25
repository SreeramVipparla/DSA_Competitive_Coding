
/**
 * QUESTION

According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

 

Example 1:


Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
Example 2:


Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.

 */


 /**
 * ANSWER
 */
import java.io.*;
import java.util.*;

public class Game_of_Life {

  public void gameOfLife(int[][] board) {
    if (board == null || board.length == 0) {
        return;
    }
    int m = board.length;
    int n = board[0].length;

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            int count = getNeighbors(board, i, j, m , n);
            if (count == 3 || board[i][j] + count == 3) {
                board[i][j] ^= 2;
            }
        }
    }
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            board[i][j] = board[i][j] >> 1;
        }
    }
}

private int getNeighbors(int[][] board, int i, int j, int m, int n) {
    int result = 0;
    for (int x = Math.max(i-1, 0); x < Math.min(i+2, m); x++) {
        for (int y = Math.max(j-1, 0); y < Math.min(j+2, n); y++) {
            result += (board[x][y] & 1);
        }
    }
    return result - (board[i][j] & 1);
}

}
 /**
 * SOURCE-LEETCODE
 */