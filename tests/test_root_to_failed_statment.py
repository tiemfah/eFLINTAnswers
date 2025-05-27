import unittest

from algorithms.root_to_failed_statement import root_to_failed_statement
from model import *


class RootToFailedStatementTestCase(unittest.TestCase):
    def test_or_1(self):
        node_a = Node("A")
        node_b = Node("B")
        node_c = Node("C")
        node_d = Node("D")
        or_node = OrNode()
        node_a.dependencies.append(node_b)
        node_b.dependencies.append(or_node)
        or_node.dependencies.append(node_c)
        or_node.dependencies.append(node_d)

        expected = "(not_C && not_D)"
        actual = root_to_failed_statement(node_a)

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

        # Or2(D, E)
        or_node_2.dependencies.append(node_d)
        or_node_2.dependencies.append(node_e)

        expected = "((not_B && not_C) || (not_D && not_E))"
        actual = root_to_failed_statement(node_a)
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

        expected = "(not_C || not_D)"
        actual = root_to_failed_statement(node_a)
        self.assertEqual(actual, expected)

    def test_human(self):
        human_node = Node("human")
        or_node_1 = OrNode()
        intelligent_node = Node("intelligent")
        and_node_1 = AndNode()
        featherless_node = Node("featherless")
        biped_node = Node("biped")
        equal_node = EqualsNode()
        number_of_legs_node = Node("number_of_legs")
        two_node = Node("2")

        human_node.dependencies.append(or_node_1)
        or_node_1.dependencies.append(intelligent_node)
        or_node_1.dependencies.append(and_node_1)
        and_node_1.dependencies.append(featherless_node)
        and_node_1.dependencies.append(biped_node)
        biped_node.dependencies.append(equal_node)
        equal_node.dependencies.append(number_of_legs_node)
        equal_node.left = number_of_legs_node
        equal_node.dependencies.append(two_node)
        equal_node.right = two_node

        expected = "((number_of_legs != 2 || not_featherless) && not_intelligent)"
        actual = root_to_failed_statement(human_node)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
