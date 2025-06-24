import unittest

from algorithms.branch_to_success_condition import branch_to_success_condition
from model import *


class BranchToSuccessConditionTestCase(unittest.TestCase):
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

        input = {node_a, node_b, or_node, node_c}
        expected = "(C)"
        actual = branch_to_success_condition(input)

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

        input = {node_a, and_node, or_node_1, or_node_2, node_b, node_d}
        expected = "(B && D)"
        actual = branch_to_success_condition(input)
        self.assertEqual(actual, expected)

    def test_or_3(self):
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

        input = {node_a, and_node, or_node_1, or_node_2, node_b, node_e}
        expected = "(B && E)"
        actual = branch_to_success_condition(input)
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

        input = {node_a, node_b, and_node, node_c, node_d}
        expected = "(C && D)"
        actual = branch_to_success_condition(input)
        self.assertEqual(actual, expected)

    def test_not_node(self):
        node_a = Node("A")
        not_node = NotNode()
        node_a.dependencies.append(not_node)
        not_node.dependencies.append(Node("B"))
        input = {node_a, not_node, not_node.dependencies[0]}
        expected = "(!(B))"
        actual = branch_to_success_condition(input)
        self.assertEqual(actual, expected)

    def test_lesser_node(self):
        node_a = Node("A")
        lesser_node = LesserNode()
        node_a.dependencies.append(lesser_node)
        left = Node("x")
        right = Node("y")
        lesser_node.dependencies.append(left)
        lesser_node.left = left
        lesser_node.dependencies.append(right)
        lesser_node.right = right
        input = {node_a, lesser_node, left, right}
        expected = "(x < y)"
        actual = branch_to_success_condition(input)
        self.assertEqual(actual, expected)

    def test_lesser_or_equal_node(self):
        node_a = Node("A")
        lesser_eq_node = LesserOrEqualNode()
        node_a.dependencies.append(lesser_eq_node)
        left = Node("x")
        right = Node("y")
        lesser_eq_node.dependencies.append(left)
        lesser_eq_node.left = left
        lesser_eq_node.dependencies.append(right)
        lesser_eq_node.right = right
        input = {node_a, lesser_eq_node, left, right}
        expected = "(x <= y)"
        actual = branch_to_success_condition(input)
        self.assertEqual(actual, expected)

    def test_greater_node(self):
        node_a = Node("A")
        greater_node = GreaterNode()
        node_a.dependencies.append(greater_node)
        left = Node("x")
        right = Node("y")
        greater_node.dependencies.append(left)
        greater_node.left = left
        greater_node.dependencies.append(right)
        greater_node.right = right
        input = {node_a, greater_node, left, right}
        expected = "(x > y)"
        actual = branch_to_success_condition(input)
        self.assertEqual(actual, expected)

    def test_greater_or_equal_node(self):
        node_a = Node("A")
        greater_eq_node = GreaterOrEqualNode()
        node_a.dependencies.append(greater_eq_node)
        left = Node("x")
        right = Node("y")
        greater_eq_node.dependencies.append(left)
        greater_eq_node.left = left
        greater_eq_node.dependencies.append(right)
        greater_eq_node.right = right
        input = {node_a, greater_eq_node, left, right}
        expected = "(x >= y)"
        actual = branch_to_success_condition(input)
        self.assertEqual(actual, expected)

    def test_empty_input(self):
        input = set()
        expected = ""
        actual = branch_to_success_condition(input)
        self.assertEqual(actual, expected)

    def test_multiple_roots(self):
        node_a = Node("A")
        node_b = Node("B")
        input = {node_a, node_b}
        expected = "(A && B)"
        actual = branch_to_success_condition(input)
        self.assertEqual(actual, expected)

    def test_human_1(self):
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
        equal_node.dependencies.append(two_node)

        input = {human_node, or_node_1, intelligent_node}
        expected = "(intelligent)"
        actual = branch_to_success_condition(input)
        self.assertEqual(actual, expected)

    def test_human_2(self):
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

        input = {human_node, or_node_1, and_node_1, featherless_node, biped_node, equal_node, number_of_legs_node}
        expected = "(featherless && number_of_legs == 2)"
        actual = branch_to_success_condition(input)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
