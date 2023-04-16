from __future__ import annotations

class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left: Node = None
        self.right: Node = None
        self.ht = 0
    
    def __str__(self) -> str:
        return f"{self.val}(BF={self.get_balance()})"
    
    def get_balance(self) -> int:
        # To complete
        return 0

def insert(root: Node, val: int):
    # To complete
    return root

def in_order_traversal(root):
    """Just a recursive DFS to get nodes with in-order traversal"""
    if root is None:
        return []
    return in_order_traversal(root.left) + [root] + in_order_traversal(root.right)

def pre_order_traversal(root):
    """Just a recursive DFS to get nodes with pre-order traversal"""
    if root is None:
        return []
    return [root] + pre_order_traversal(root.left) + pre_order_traversal(root.right)

if __name__ == "__main__":
    root = None

    N = int(input())

    for val in map(int, input().split()):
        root = insert(root, val)
    
    root = insert(root, int(input()))
    
    print(*in_order_traversal(root))
    print(*pre_order_traversal(root))