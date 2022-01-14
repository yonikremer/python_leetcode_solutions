# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if val > root.val:
            return TreeNode(val=val, left=root)
        return self.insert_to_max_tree_rec(parent=None, root=root, val=val)

    def insert_to_max_tree_rec(self, parent: Optional[TreeNode], root: Optional[TreeNode], val: int,
                               left: bool = True) -> Optional[TreeNode]:
        if isinstance(parent, TreeNode):
            assert parent.val > val
        if not isinstance(root, TreeNode):
            return TreeNode(val=val)
        if val > root.val:
            new_root = TreeNode(val=val, left=root)
            if left:
                parent.left = new_root
            else:
                parent.right = new_root
            return new_root
        root.right = self.insert_to_max_tree_rec(parent=root, root=root.right, val=val, left=False)
        return root


if __name__ == "__main__":
    s = Solution()
    s.insert_into_max_tree([5, 2, 4, None, 1])
