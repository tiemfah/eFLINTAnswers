import unittest

from algorithms.branch_to_negated_condition import branch_to_negated_condition
from model import *


class BranchToNegatedStatementTestCase(unittest.TestCase):
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
        expected = "(not_C)"
        actual = branch_to_negated_condition(input)

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
        expected = "(not_B || not_D)"
        actual = branch_to_negated_condition(input)
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
        expected = "(not_B || not_E)"
        actual = branch_to_negated_condition(input)
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
        expected = "(not_C || not_D)"
        actual = branch_to_negated_condition(input)
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
        expected = "(not_intelligent)"
        actual = branch_to_negated_condition(input)
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
        expected = "(not_featherless || number_of_legs != 2)"
        actual = branch_to_negated_condition(input)
        self.assertEqual(actual, expected)

    def test_circular_dependency(self):
        node_a = Node("A")
        node_b = Node("B")
        node_a.dependencies.append(node_b)
        node_b.dependencies.append(node_a)
        input = {node_a, node_b}
        actual = branch_to_negated_condition(input)
        self.assertTrue(actual.startswith("(not_"))

    def test_not_node(self):
        node_a = Node("A")
        not_node = NotNode()
        not_node.dependencies.append(node_a)
        input = {not_node, node_a}
        actual = branch_to_negated_condition(input)
        self.assertEqual(actual, "(!(not_A))")

    def test_lesser_node(self):
        left = Node("X")
        right = Node("Y")
        lesser_node = LesserNode()
        lesser_node.left = left
        lesser_node.right = right
        lesser_node.dependencies.append(left)
        lesser_node.dependencies.append(right)
        input = {lesser_node, left, right}
        actual = branch_to_negated_condition(input)
        self.assertEqual(actual, "(X >= Y)")

    def test_lesser_or_equal_node(self):
        left = Node("X")
        right = Node("Y")
        node = LesserOrEqualNode()
        node.left = left
        node.right = right
        node.dependencies.append(left)
        node.dependencies.append(right)
        input = {node, left, right}
        actual = branch_to_negated_condition(input)
        self.assertEqual(actual, "(X > Y)")

    def test_greater_node(self):
        left = Node("X")
        right = Node("Y")
        node = GreaterNode()
        node.left = left
        node.right = right
        node.dependencies.append(left)
        node.dependencies.append(right)
        input = {node, left, right}
        actual = branch_to_negated_condition(input)
        self.assertEqual(actual, "(X <= Y)")

    def test_greater_or_equal_node(self):
        left = Node("X")
        right = Node("Y")
        node = GreaterOrEqualNode()
        node.left = left
        node.right = right
        node.dependencies.append(left)
        node.dependencies.append(right)
        input = {node, left, right}
        actual = branch_to_negated_condition(input)
        self.assertEqual(actual, "(X < Y)")

    def test_else_fallback(self):
        # Node with dependencies, but not matching any if/elif
        class CustomNode(Node):
            pass

        node_a = Node("A")
        custom_node = CustomNode("custom")
        custom_node.dependencies.append(node_a)
        input = {custom_node, node_a}
        actual = branch_to_negated_condition(input)
        self.assertEqual(actual, "(not_A)")

    def test_node_without_dependency(self):
        node_a = Node("A")
        input = {node_a}
        actual = branch_to_negated_condition(input)
        self.assertEqual(actual, "(not_A)")

    def test_empty_branch(self):
        self.assertEqual(branch_to_negated_condition(set()), "")

if __name__ == '__main__':
    unittest.main()
