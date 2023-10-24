# Binary Tree Preorder Traversal
# Iterative Solution -->

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        curr, stack = root, []
        result = []

        while curr or stack:

            if curr:
                result.append(curr.val)
                stack.append(curr.right)
                curr = curr.left
            
            else:
                curr = stack.pop()
                
        return result