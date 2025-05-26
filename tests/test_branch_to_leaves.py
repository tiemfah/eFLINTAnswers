import unittest

from algorithms.branch_to_leaves import branch_to_leaves
from model import *


class BranchToLeavesTestCase(unittest.TestCase):

    def test_base_case(self):
        node_a = Node("A")
        node_b = Node("B")
        node_c = Node("C")
        node_d = Node("D")
        and_node = AndNode()
        node_a.dependencies.append(node_b)
        node_b.dependencies.append(and_node)
        and_node.dependencies.append(node_c)
        and_node.dependencies.append(node_d)

        input = {node_a, node_b, and_node, node_c, node_d}
        expected = {node_c, node_d}
        actual = branch_to_leaves(input)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
