import pytest

from BST import BST

class TestBST:
    def test_node_creation(self):
        test_value = 50
        test_bst = BST(test_value)
        assert test_bst.root.value == test_value

    def test_print_inorder(self, capfd):
        test_value = 50
        test_bst = BST(test_value)
        test_bst.insert(40)
        test_bst.insert(60)
        test_bst.print_inorder()
        out, _ = capfd.readouterr()
        actual_result = out.strip()
        expected_result = str([40, 50, 60])
        assert actual_result == expected_result

