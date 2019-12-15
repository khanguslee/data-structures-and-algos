class Node:
    def __init__(self, input_value):
        self.left = None
        self.right = None
        self.value = input_value

class BST:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def insert(self, input_value):
        self.insert_recurse(self.root, input_value)

    def insert_recurse(self, input_node, input_value):
        if input_node is None:
            return Node(input_value)
        else:
            if input_value < input_node.value:
                self.insert_recurse(input_node.left, input_value)
            elif input_value > input_node.value:
                self.insert_recurse(input_node.right, input_value)
            else:
                raise ValueError("Duplicate Value")

    def search(self, input_value):
        # TODO: Search for a value
        pass

    def delete(self, input_value):
        # TODO: Delete value from tree
        pass

if __name__ == "__main__":
     binary_search_tree = BST(50)
     binary_search_tree.insert(70)
     binary_search_tree.insert(10)
     print(binary_search_tree)
