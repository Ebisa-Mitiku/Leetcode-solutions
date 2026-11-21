# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not preorder or not inorder:
            return None

        root_value = preorder[0]

        root = TreeNode(root_value)

        mid = inorder.index(root_value)

        root.left = self.buildTree(
            preorder[1:mid+1],
            inorder[:mid]
        )

        root.right = self.buildTree(
            preorder[mid+1:],
            inorder[mid+1:]
        )

        return root