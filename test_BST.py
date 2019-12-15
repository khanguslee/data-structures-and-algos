import pytest

from BST import BST


class TestBST:
    def test_node_creation(self):
        test_value = 50
        test_bst = BST(test_value)
        assert test_bst.root.value == test_value

    def test_print_inorder(self, capfd):
        # Generate test BST
        test_value = 50
        test_bst = BST(test_value)
        test_bst.insert(60)
        test_bst.insert(10)
        test_bst.insert(20)
        test_bst.insert(30)
        test_bst.insert(5)
        test_bst.print_inorder()

        # Check output
        out, _ = capfd.readouterr()
        actual_result = out.strip()
        expected_result = str([5, 10, 20, 30, 50, 60])
        assert actual_result == expected_result

    def test_print_preorder(self, capfd):
        # Generate test BST
        test_value = 50
        test_bst = BST(test_value)
        test_bst.insert(60)
        test_bst.insert(10)
        test_bst.insert(20)
        test_bst.insert(30)
        test_bst.insert(5)
        test_bst.print_preorder()

        # Check output
        out, _ = capfd.readouterr()
        actual_result = out.strip()
        expected_result = str([50, 10, 5, 20, 30, 60])
        assert actual_result == expected_result

    def test_print_postorder(self, capfd):
        # Generate test BST
        test_value = 50
        test_bst = BST(test_value)
        test_bst.insert(60)
        test_bst.insert(10)
        test_bst.insert(20)
        test_bst.insert(30)
        test_bst.insert(5)
        test_bst.print_postorder()

        # Check output
        out, _ = capfd.readouterr()
        actual_result = out.strip()
        expected_result = str([5, 30, 20, 10, 60, 50])
        assert actual_result == expected_result
