# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Leetcode 104 - https://leetcode.com/problems/maximum-depth-of-binary-tree/
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 1)]
        maxdepth = 0

        # iterative dfs
        while stack:
            node,depth = stack.pop()
            if node:
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
                maxdepth = max(maxdepth, depth)

        return maxdepth