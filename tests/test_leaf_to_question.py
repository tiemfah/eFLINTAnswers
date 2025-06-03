import unittest

from algorithms.leaf_to_question import leaf_to_question
from model import Node


class LeafToQuestionTestCase(unittest.TestCase):

    def test_int_node(self):
        node = Node("number_of_legs")
        node_to_type_map = {"number_of_legs": "int"}
        expected = '"How many number of legs does the actor have?" number_of_legs: int'
        actual = leaf_to_question(node, node_to_type_map)
        self.assertEqual(actual, expected)

    def test_bool_node(self):
        node = Node("intelligent")
        node_to_type_map = {"intelligent": "bool"}
        expected = '"Is the actor intelligent?" intelligent: bool\n"Is the actor not intelligent?" not_intelligent: bool'
        actual = leaf_to_question(node, node_to_type_map)
        self.assertEqual(actual, expected)

    def test_string_node(self):
        node = Node("name")
        node_to_type_map = {"name": "string"}
        expected = '"What is the actor name?" name: str'
        actual = leaf_to_question(node, node_to_type_map)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
