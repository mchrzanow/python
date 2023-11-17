import os

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)

class Tree:
    def __init__(self, root_path):
        self.root = Node(root_path)
        self._build_tree(self.root, root_path)

    def _build_tree(self, node, path):
        if not os.path.exists(path):
            raise FileNotFoundError(f"Directory '{path}' does not exist.")

        if os.path.isdir(path):
            items = sorted(os.listdir(path))  # Sort the items for consistent order
            for item in items:
                item_path = os.path.join(path, item)
                child_node = Node(item)
                node.add_child(child_node)
                self._build_tree(child_node, item_path)

    def __str__(self, depth=None):
        return self._str_node(self.root, 0, depth)

    def _str_node(self, node, level, depth):
        if depth is not None and level >= depth:
            return ""
        ret = "\t" * level + repr(node.value) + "\n"
        for child in node.children:
            ret += self._str_node(child, level + 1, depth)
        return ret

#Użycie:
#tree = Tree('C:/Users/micha/OneDrive/Pulpit/studia/semestr 7')
#print(tree.__str__(3))
