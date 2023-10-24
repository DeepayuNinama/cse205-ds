# 94. Binary Tree Inorder Traversal
# Recursive Solution -->

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # Resursive Approach -->
        res = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        return res
