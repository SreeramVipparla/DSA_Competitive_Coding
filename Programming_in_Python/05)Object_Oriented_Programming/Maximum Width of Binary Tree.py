"""
QUESTION-
Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes are also counted into the length calculation.

It is guaranteed that the answer will in the range of 32-bit signed integer.

 

Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
Example 2:


Input: root = [1,3,null,5,3]
Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).
Example 3:


Input: root = [1,3,2,5]
Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).
 

Constraints:

The number of nodes in the tree is in the range [1, 3000].
-100 <= Node.val <= 100
"""
"""
ANSWER-
"""
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        queue, result = [], 1
        queue.append([root, 1])
        while queue:
            tmp = []
            result = max(result, queue[-1][1] - queue[0][1] + 1)
            for [node, pos] in queue:
                if node.left: tmp.append([node.left, pos*2])
                if node.right: tmp.append([node.right, pos*2 + 1])
            queue = tmp
        return result
        
"""
SOURCE-LEETCODE
"""