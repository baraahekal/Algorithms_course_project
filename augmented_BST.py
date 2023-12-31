class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.left = self.right = None
        self.size = 1  # Augmentation


# Function time-complexity in case of Balanced BST: Θ(log(n))
def insert(root, key) -> Node:
    if not root:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    root.size = 1 + size(root.left) + size(root.right)  # Update size
    return root


# Function time-complexity: Θ(1)
def size(node) -> int:
    return node.size if node else 0


# Function time-complexity in case of Balanced BST: Θ(log(n))
def rank(x, root) -> int:
    node_rank = 0
    current = root

    while current:
        if x <= current.key:
            current = current.left
        else:
            node_rank += size(current.left) + 1
            current = current.right

    return node_rank


# Function time-complexity in case of Balanced BST: Θ(log(n))
def contains(x, root) -> bool:
    current = root

    while current:
        if x == current.key:
            return True
        elif x < current.key:
            current = current.left
        else:
            current = current.right

    return False


def main():
    values = [35, 11, 42, 9, 27, 36, 68, 5, 22, 30, 39, 57, 80]
    root = None
    for value in values:
        root = insert(root, value)

    low = 9
    hi = 57

    result = rank(hi, root) - rank(low, root) + 1 if contains(hi, root) else rank(hi, root) - rank(low, root)
    print(result)


if __name__ == '__main__':
    main()
