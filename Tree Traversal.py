class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.value = data


def in_order(root):
    if root is None:
        return
    in_order(root.left)
    print(root.value)
    in_order(root.right)


def pre_order(root):
    if root is None:
        return
    print(root.value)
    pre_order(root.left)
    pre_order(root.right)


def post_order(root):
    if root is None:
        return
    pre_order(root.left)
    post_order(root.right)
    print(root.value)


def height(root):
    if root is None:
        return -1
    left_height = height(root.left)
    right_height = height(root.right)

    return max(left_height, right_height) + 1


def print_given_level(root, level):
    if root is None:
        return

    if level == 1:
        print(root.value)
    elif level > 1:
        print_given_level(root.left, level-1)
        print_given_level(root.right, level-1)


def level_order_traversal(root):
    h = height(root)
    print(h)

    for i in range(1, h+2):  # h+2 because of the nodes
        print_given_level(root, i)


def level_order_using_queue(root):
    queue = list()
    queue.append(root)
    while root and len(queue) >= 1:
        root = queue.pop(0)
        print(root.value)
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)


def reverse_order_using_queue(root):
    queue = list()
    stack = list()
    queue.append(root)
    while root and len(queue) >= 1:
        root = queue.pop(0)
        stack.append(root)
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)

    while len(stack) > 0:
        print(stack.pop().value)


def is_leaf(node):  # To check if its a leaf node
    if node.right and node.left is None:
        return True
    else:
        return False


def find_nodes_at_dist_q50(node, path, dict_nodes, dist):
    # Empty tree and base condition
    if node is None:
        return

    if is_leaf(node) and len(path) >= dist:
        dict_nodes[len(path) - dist] = node
        return
    path.append(node)
    find_nodes_at_dist_q50(node.right, path, dict_nodes, dist)
    find_nodes_at_dist_q50(node.left, path, dict_nodes, dist)


rootNode = Node(1)
rootNode.left = Node(2)
rootNode.right = Node(3)
rootNode.left.left = Node(4)
rootNode.left.right = Node(5)
rootNode.right.left = Node(6)
rootNode.right.right = Node(7)

level_order_using_queue(rootNode)
reverse_order_using_queue(rootNode)
path = list()
path.append(rootNode)
dict_nodes = dict()

find_nodes_at_dist_q50(rootNode, path, dict_nodes, 1)





