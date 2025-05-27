from textwrap import dedent, indent

from algorithms.branch_to_leaves import branch_to_leaves
from algorithms.branch_to_negated_condition import branch_to_negated_condition
from algorithms.branch_to_success_condition import branch_to_success_condition
from algorithms.leaf_to_question import leaf_to_question
from algorithms.root_to_branches import root_to_branches
from algorithms.root_to_failed_statement import root_to_failed_statement
from model import Node, ALL_NODE_TYPES


def root_to_liveql(root: Node, node_to_type_map: dict[str, str]) -> str:
    """
    algorithm map-to-LiveQL
        input: root
        output: LiveQL DSL string

        branches <- call root-to-branches with root
        branches <- call ascending sort branches with size as key

        liveql <- empty string
        for each branch in branches do

            leaves <- call branch-to-leaves with branches
            for each leaf in leaves do
                question-line <- call leaf-to-question with leaf
                add liveql with question-line

            success-condition <- call branch-to-success-condition with branch
            add liveql with success-condition

            negated-condition <- call branch-to-negated-condition with branch
            add liveql with negated-condition

        root-failed-statement <- call root-to-failed-statement with root
        add liveql with root-to-failed-statement
    """

    """
    form humanForm {
        "Is the actor intelligent?" intelligent: bool
        "Is the actor not intelligent?" not_intelligent: bool
        if (intelligent) {
            "Property human holds" result: bool(true)"
        }
        if (not_intelligent) {
            "Is the actor featherless?" featherless: bool
            "Is the actor not featherless?" not_featherless: bool
    
            "How many number of legs does the actor have?": number_of_legs: int
        }
        if (featherless && number_of_legs == 2) {
            "Property human holds" result: bool(true)"
        }
        if (not_intelligent && (not_featherless || number_of_legs != 2)) {
            "Property human does not holds" result: bool(true)"
        }
    }
    """
    branches = root_to_branches(root)
    branches = sorted(branches, key=len)
    questions_and_success_condition = consume_branches(root, branches, node_to_type_map)
    final_fail_statement = get_final_failed_statement(root)
    return "\n".join([
        f'form {root.name}Form {{',
        f'{indent(questions_and_success_condition, "\t")}',
        f'{indent(final_fail_statement, "\t")}',
        f'}}'
    ])


def get_if_success_holds(root: Node, success_condition: str) -> str:
    return dedent(f'''
        if {success_condition} {{
            "Property {root.name} holds" result: bool(true)
        }}''')


def get_if_negated_go_to_next_set_of_question(negated_condition: str, inner_text: str) -> str:
    return dedent(f'''
if {negated_condition} {{
{inner_text}
}}''')


def get_final_failed_statement(root: Node) -> str:
    return dedent(f'''
        if {root_to_failed_statement(root)} {{
            "Property {root.name} does not holds" result: bool(true)
        }}''')


def get_question_from_branch(branch: set[ALL_NODE_TYPES], node_to_type_map: dict[str, str]) -> str:
    return "\n".join([leaf_to_question(leaf, node_to_type_map) for leaf in branch_to_leaves(branch)])


def consume_branches(root: Node, branches: list[set[ALL_NODE_TYPES]], node_to_type_map: dict[str, str]) -> str:
    if branches:
        current_branch = branches[0]
        return "\n".join([
            f'{get_question_from_branch(current_branch, node_to_type_map)}',
            f'{get_if_success_holds(root, branch_to_success_condition(current_branch))}',
            f'{get_if_negated_go_to_next_set_of_question(branch_to_negated_condition(current_branch), consume_branches(root, branches[1:], node_to_type_map)) if len(branches) > 1 else ""}',
        ])
    return ""
