import unittest

from algorithms.root_to_branches import root_to_branches
from model import *


class RootToBranchesTestCase(unittest.TestCase):

    def test_or(self):
        node_a = Node("A")
        node_b = Node("B")
        node_c = Node("C")
        node_d = Node("D")
        or_node = OrNode()
        node_a.dependencies.append(node_b)
        node_b.dependencies.append(or_node)
        or_node.dependencies.append(node_c)
        or_node.dependencies.append(node_d)

        actual = root_to_branches(node_a)
        expected = [
            {node_a, node_b, or_node, node_c},
            {node_a, node_b, or_node, node_d},
        ]
        self.assertEqual(actual, expected)

    def test_or_2(self):
        node_a = Node("A")
        node_b = Node("B")
        node_c = Node("C")
        node_d = Node("D")
        node_e = Node("E")
        and_node = AndNode()
        or_node_1 = OrNode()
        or_node_2 = OrNode()

        # A -> And(Or1, Or2)
        node_a.dependencies.append(and_node)
        and_node.dependencies.append(or_node_1)
        and_node.dependencies.append(or_node_2)

        # Or1(B, C)
        or_node_1.dependencies.append(node_b)
        or_node_1.dependencies.append(node_c)

        # Or2(B, C)
        or_node_2.dependencies.append(node_d)
        or_node_2.dependencies.append(node_e)

        actual = root_to_branches(node_a)
        expected = [
            {node_a, and_node, or_node_1, or_node_2, node_b, node_d},
            {node_a, and_node, or_node_1, or_node_2, node_b, node_e},
            {node_a, and_node, or_node_1, or_node_2, node_c, node_d},
            {node_a, and_node, or_node_1, or_node_2, node_c, node_e},
        ]
        self.assertEqual(actual, expected)

    def test_and(self):
        node_a = Node("A")
        node_b = Node("B")
        node_c = Node("C")
        node_d = Node("D")
        and_node = AndNode()
        node_a.dependencies.append(node_b)
        node_b.dependencies.append(and_node)
        and_node.dependencies.append(node_c)
        and_node.dependencies.append(node_d)

        actual = root_to_branches(node_a)
        expected = [
            {node_a, node_b, and_node, node_c, node_d},
        ]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
