# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(node, sumsofar):
  if not node:
    return sumsofar
  left = dfs(node.left, sumsofar + 1)
  right = dfs(node.right, sumsofar + 1)
  return max(left, right)

def count_levels(root):
  result = dfs(root, 0)
  return result

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree max depth: " + str(count_levels(root)))
  root.right.right.left = TreeNode(21)
  print("Tree max depth: " + str(count_levels(root)))

main()