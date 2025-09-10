# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, res , root):
        if not root:
            return 
        self.helper(res, root.left)
        res.append(root.val)
        self.helper(res,root.right)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res= []
        self.helper(res,root)
        return res