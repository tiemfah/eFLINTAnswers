import re
import unittest

from algorithms.root_to_liveql import root_to_liveql
from eflint.eflint_parser import get_node_to_type_map, create_graph
from tests.resources.human_eflint_types import HUMAN_EFLINT_TYPES


class E2ETestCase(unittest.TestCase):
    def test_human(self):
        node_to_type_map = get_node_to_type_map(HUMAN_EFLINT_TYPES)
        graph = create_graph(HUMAN_EFLINT_TYPES)
        human_node = graph["human"]
        actual = root_to_liveql(human_node, node_to_type_map)
        expected = """
        form humanForm {
            "Is the actor intelligent?" intelligent: bool
            "Is the actor not intelligent?" not_intelligent: bool
            if (intelligent) {
                "Property human holds" result: bool(true)
            }
            if (not_intelligent) {
                "Is the actor featherless?" featherless: bool
                "Is the actor not featherless?" not_featherless: bool
                "How many number of legs does the actor have?" number_of_legs: int
                if (number_of_legs == 2 && featherless) {
                    "Property human holds" result: bool(true)
                }
                if ((number_of_legs != 2 || not_featherless) && not_intelligent) {
                    "Property human does not holds" result: bool(true)
                }
            }
        }
        """
        self.assertEqual(
            re.sub(r"\s+", "", expected),
            re.sub(r"\s+", "", actual)
        )


if __name__ == '__main__':
    unittest.main()
