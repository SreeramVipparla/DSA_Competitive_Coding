"""
QUESTION-

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 
"""
"""
ANSWER-
"""
from collections import defaultdict


class TrieNode:
    
    def __init__(self, end_of_word=False):
        self.end_of_word = end_of_word
        self.children = defaultdict(TrieNode)
    

class Trie:
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        current = self.root
        for character in word:
            current = current.children[character]
        current.end_of_word = True
        
        
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #valid both inputs
        if not self.is_valid_word(word):
            return False
        if not self.is_valid_board(board):
            return False
        
        #instantiate trie and insert the word
        trie = Trie()
        trie.insert(word)
        
        return self.dfs(trie, board, word)
    
    def is_valid_word(self, word):
        if word == "" or word is None or not isinstance(word, str):
            return False
        return True
        
    def is_valid_board(self, board):
        if len(board) == 0 or not isinstance(board, list) or board is None:
            return False
        return True
    
    def dfs(self, trie, board, word):
        #only perform dfs if the character is the first character in the given word
        for row_index, row in enumerate(board):
            for col_index, value in enumerate(row):
                if value == word[0]:
                    if self.dfs_visit(trie.root, row_index, col_index, board):
                        return True
        return False
    
    def dfs_visit(self, trie_node, row_index, col_index, board):
        
        #get the current character
        char = board[row_index][col_index]
        
        #check to see if current character is a child of the previous trie node
        if char not in trie_node.children:
            return False
        
        #check trie to see if you are at the end of a word
        if trie_node.children[char].end_of_word:
            return True
        
        #mark character as visited
        board[row_index][col_index] = "<Visited>"
        
        #visit all neighbors that haven't been already been visited
        for row, col in self.get_neighbors(board, row_index, col_index):
            if board[row][col] != "<Visited>":
                if self.dfs_visit(trie_node.children[char], row, col, board):
                    return True
                
        #unmark character as visited
        board[row_index][col_index] = char
        return False
    
    #only returns indices that are within the grid
    def get_neighbors(self, board, row, col):
        num_cols = len(board[0])
        num_rows = len(board)
        for nr, nc in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
            if nr != - 1 and nc != -1 and nr <= num_rows - 1 and nc <= num_cols - 1:
                yield nr, nc
"""
SOURCE-LEETCODE
"""