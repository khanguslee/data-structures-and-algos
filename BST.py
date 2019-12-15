class Node:
    def __init__(self, input_value):
        self.left = None
        self.right = None
        self.value = input_value


class BST:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def insert(self, input_value):
        self.root = self.insert_recurse(self.root, input_value)

    def insert_recurse(self, input_node, input_value):
        if input_node is None:
            input_node = Node(input_value)
        else:
            if input_value < input_node.value:
                input_node.left = self.insert_recurse(
                    input_node.left, input_value)
            elif input_value > input_node.value:
                input_node.right = self.insert_recurse(
                    input_node.right, input_value)
            else:
                raise ValueError("Duplicate Value")
        return input_node

    def __contains__(self, input_value):
        return self._contains_recurse(self.root, input_value)

    def _contains_recurse(self, input_node, input_value):
        if input_node is None:
            return False
        elif input_node.value == input_value:
            return True
        elif input_value < input_node.value:
            return self._contains_recurse(input_node.left, input_value)
        elif input_value > input_node.value:
            return self._contains_recurse(input_node.right, input_value)
            

    def delete(self, input_value):
        # TODO: Delete value from tree
        pass

    def find_min(self):
        current_node = self.root
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def print_inorder(self):
        output_array = []
        output_array = self._print_inorder_recurse(self.root, output_array)
        print(output_array)

    def _print_inorder_recurse(self, input_node, input_array):
        if input_node is not None:
            input_array = self._print_inorder_recurse(
                input_node.left, input_array)
            input_array.append(input_node.value)
            input_array = self._print_inorder_recurse(
                input_node.right, input_array)
        return input_array

    def print_preorder(self):
        output_array = []
        output_array = self._print_preorder_recurse(self.root, output_array)
        print(output_array)

    def _print_preorder_recurse(self, input_node, input_array):
        if input_node is not None:
            input_array.append(input_node.value)
            input_array = self._print_preorder_recurse(
                input_node.left, input_array)
            input_array = self._print_preorder_recurse(
                input_node.right, input_array)
        return input_array

    def print_postorder(self):
        output_array = []
        output_array = self._print_postorder_recurse(self.root, output_array)
        print(output_array)

    def _print_postorder_recurse(self, input_node, input_array):
        if input_node is not None:
            input_array = self._print_postorder_recurse(
                input_node.left, input_array)
            input_array = self._print_postorder_recurse(
                input_node.right, input_array)
            input_array.append(input_node.value)
        return input_array


if __name__ == "__main__":
    binary_search_tree = BST(50)
    binary_search_tree.insert(70)
    binary_search_tree.insert(10)
    binary_search_tree.insert(20)
    binary_search_tree.insert(30)
    binary_search_tree.insert(5)

    binary_search_tree.print_inorder()
