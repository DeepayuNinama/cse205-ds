# Binary Tree Preorder Traversal
# Recursive Solution -->

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List:
        if not root:
            return []
        self.result = []
        self.helper(root)
        return self.result
        
    def helper(self,root):
        if root:
            self.result.append(root.val)
            self.helper(root.left)
            self.helper(root.right)