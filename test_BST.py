import pytest

from BST import BST

class TestBST:
    def test_node_creation(self):
        test_value = 50
        test_bst = BST(test_value)
        assert test_bst.root.value == test_value