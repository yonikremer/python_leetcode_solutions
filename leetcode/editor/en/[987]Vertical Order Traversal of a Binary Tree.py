# leetcode submit region begin(Prohibit modification and deletion)
from typing import Optional, List, Dict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.d: Dict[int, Dict[int, List[int]]] = dict([])  # Maps int i to the dict of values for the nodes in the ith column.

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        self.traverse_rec(root, 0, 0)
        ans: List[List[int]] = []
        column: int
        for column in sorted(self.d.keys()):
            col_list: List[int] = []
            col_dict: Dict[int, int] = self.d[column]
            for row in sorted(col_dict.keys()):
                col_list += sorted(col_dict[row])
            ans.append(col_list)
        return ans

    def traverse_rec(self, root: Optional[TreeNode], row: int, col: int):
        if root is None:
            return
        if col in self.d.keys():
            column = self.d[col]
            if row not in column.keys():
                column[row] = [root.val]
            else:
                column[row].append(root.val)
        else:
            column = dict()
            if row not in column.keys():
                column[row] = [root.val]
            else:
                column[row].append(root.val)
            self.d[col] = column
        self.traverse_rec(root.left, row + 1, col - 1)
        self.traverse_rec(root.right, row + 1, col + 1)
# leetcode submit region end(Prohibit modification and deletion)
