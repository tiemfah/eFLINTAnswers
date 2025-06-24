import unittest
from collections import defaultdict

from algorithms.root_to_liveql import root_to_liveql
from eflint.eflint_parser import get_node_to_type_map, get_parameter_facts, create_graph
from tests.resources.aow_eflint_facts import AOW_EFLINT_FACTS
from tests.resources.aow_eflint_types import AOW_EFLINT_TYPES
from tests.resources.human_eflint_facts import HUMAN_EFLINT_FACTS
from tests.resources.human_eflint_types import HUMAN_EFLINT_TYPES


class E2ETestCase(unittest.TestCase):
    def test_human(self):
        node_name_to_node = create_graph(HUMAN_EFLINT_TYPES)
        node_to_type_map = get_node_to_type_map(HUMAN_EFLINT_TYPES)
        parameter_facts = get_parameter_facts(HUMAN_EFLINT_TYPES, HUMAN_EFLINT_FACTS)
        human_node = node_name_to_node["human"]
        actual = root_to_liveql(human_node, node_to_type_map, parameter_facts)
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

        expected_freq = defaultdict(int)
        actual_freq = defaultdict(int)

        for line in expected.strip().splitlines():
            line = line.strip()
            if line:
                expected_freq[line] += 1

        for line in actual.strip().splitlines():
            line = line.strip()
            if line:
                actual_freq[line] += 1

        self.assertEqual(expected_freq, actual_freq)

    def test_income_supplement(self):
        node_name_to_node = create_graph(AOW_EFLINT_TYPES)
        node_to_type_map = get_node_to_type_map(AOW_EFLINT_TYPES)
        parameter_facts = get_parameter_facts(AOW_EFLINT_TYPES, AOW_EFLINT_FACTS)
        human_node = node_name_to_node["[Recht op IIT 591]"]
        actual = root_to_liveql(human_node, node_to_type_map, parameter_facts)
        expected = """
        form Recht_op_IIT_591Form {
            "BOVENGRENS_INKOMEN_ALLEENSTAANDE" BOVENGRENS_INKOMEN_ALLEENSTAANDE:int(1207)
            "BOVENGRENS_INKOMEN_NIET_ALLEENSTAANDE" BOVENGRENS_INKOMEN_NIET_ALLEENSTAANDE:int(1724)
            "BOVENGRENS_VERMOGEN_HOOG" BOVENGRENS_VERMOGEN_HOOG:int(12450)
            "BOVENGRENS_VERMOGEN_LAAG" BOVENGRENS_VERMOGEN_LAAG:int(6225)
            "What is the actor Woonplaats?" Woonplaats: str
            "How many Inkomen per maand does the actor have?" Inkomen_per_maand: int
            "How many leeftijd does the actor have?" leeftijd: int
            "What is the actor status?" status: str
            "How many Vermogen does the actor have?" Vermogen: int
            if (Woonplaats == "Utrecht" && !(leeftijd > 67) && leeftijd > 21 && !(status == "Geen") && Inkomen_per_maand <= BOVENGRENS_INKOMEN_NIET_ALLEENSTAANDE && Vermogen <= BOVENGRENS_VERMOGEN_HOOG) {
                "Property Recht op IIT 591 holds" result: bool(true)
            }
            if (Woonplaats != "Utrecht" || (!(leeftijd <= 67) || (leeftijd <= 21 || (!(status != "Geen") || (Inkomen_per_maand > BOVENGRENS_INKOMEN_NIET_ALLEENSTAANDE || Vermogen > BOVENGRENS_VERMOGEN_HOOG))))) {
                "Property Recht op IIT 591 does not holds" result: bool(true)
            }
        }
        """

        print(actual)

        expected_freq = defaultdict(int)
        actual_freq = defaultdict(int)

        for line in expected.strip().splitlines():
            line = line.strip()
            if line:
                expected_freq[line] += 1

        for line in actual.strip().splitlines():
            line = line.strip()
            if line:
                actual_freq[line] += 1

        self.assertEqual(expected_freq, actual_freq)

if __name__ == '__main__':
    unittest.main()
