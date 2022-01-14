from typing import Optional, List


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val: int = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


def construct_maximum_binary_tree(nums: List[int]) -> Optional[TreeNode]:
    if len(nums) == 0:
        return None
    if len(nums) == 1:
        return TreeNode(val=nums[0])
    maxi: int
    arg_maxi: int
    arg_maxi, maxi = max(list(enumerate(nums)), key=lambda x: x[1])
    assert maxi == nums[arg_maxi]
    left_list: List[int] = nums[:arg_maxi]
    right_list: List[int] = nums[arg_maxi + 1:]
    if len(left_list) > 1:
        left_node = construct_maximum_binary_tree(left_list)
    elif len(left_list) == 1:
        left_node = TreeNode(val=left_list[0])
    else:
        left_node = None
    if len(right_list) > 1:
        right_node = construct_maximum_binary_tree(right_list)
    elif len(right_list) == 1:
        right_node = TreeNode(val=right_list[0])
    else:
        right_node = None
    head = TreeNode(val=maxi, left=left_node, right=right_node)
    return head


if __name__ == "__main__":
    my_list: List[int] = [3,2,1,6,0,5]
    tree = construct_maximum_binary_tree(my_list)
