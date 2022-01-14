# leetcode submit region begin(Prohibit modification and deletion)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


class Solution:

    def __init__(self):
        self.max_path_sum: dict = {}
        # max_path_sum[i] is the maxPathSum of the ith node
        self.max_path_sum_include: dict = {}
        # max_path_sum_include[i] is the maxPathSum of the ith node

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_sum: dict = {}
        # max_path_sum[i] is the maxPathSum of the ith node
        self.max_path_sum_include: dict = {}
        # max_path_sum_include[i] is the maxPathSum of the ith node
        return self.my_max_path_sum(root, i=0)

    def my_max_path_sum(self, root: Optional[TreeNode], i: int):
        if root is None:
            return -32768
        if root.left is None and root.right is None:
            return root.val
        if i in self.max_path_sum:
            return self.max_path_sum[i]
        left_sum: int = self.my_max_path_sum(root.left, i=i * 2 + 1)
        right_sum: int = self.my_max_path_sum(root.right, i=i * 2 + 2)
        left_include = self.my_max_path_sum_include(root.left, i=i * 2 + 1)
        right_include = self.my_max_path_sum_include(root.right, i=i * 2 + 2)
        val: int = root.val
        ans = max([val, right_sum, left_sum, right_include + val, left_include + val, right_include + left_include + val])
        self.max_path_sum[i] = ans
        return ans

    def my_max_path_sum_include(self, root: Optional[TreeNode], i: int) -> int:
        if root is None:
            return -32768
        if root.left is None and root.right is None:
            return root.val
        if i in self.max_path_sum_include:
            return self.max_path_sum_include[i]
        left: Optional[TreeNode] = root.left
        right: Optional[TreeNode] = root.right
        left_include = self.my_max_path_sum_include(left, i=i * 2 + 1)
        right_include = self.my_max_path_sum_include(right, i=i * 2 + 2)
        val = root.val
        ans = max([val, right_include + val, left_include + val])
        self.max_path_sum_include[i] = ans
        return ans
# leetcode submit region end(Prohibit modification and deletion)
