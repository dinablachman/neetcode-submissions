# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        leftTree = self.treeHeight(root.left)
        rightTree = self.treeHeight(root.right)
        if abs(leftTree - rightTree) > 1:
            return False
        leftBalanced = self.isBalanced(root.left)
        rightBalanced = self.isBalanced(root.right)
        return leftBalanced and rightBalanced
    
    def treeHeight(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        return max(self.treeHeight(node.right), self.treeHeight(node.left)) + 1