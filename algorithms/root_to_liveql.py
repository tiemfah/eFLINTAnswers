from textwrap import indent

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
    branches = root_to_branches(root)
    branches = sorted(branches, key=len)
    questions_and_success_condition = consume_branches(root, branches, node_to_type_map)
    return "\n".join([
        f'form {root.to_liveql_var()}Form {{',
        f'{indent(questions_and_success_condition, "\t")}',
        f'}}'
    ])


def get_if_success_holds(root: Node, success_condition: str) -> str:
    success_statement = f'"Property {root.to_question()} holds" result: bool(true)'
    return "\n".join([
        f'if {success_condition} {{',
        indent(success_statement, "\t"),
        f'}}'
    ])


def get_if_negated_go_to_next_set_of_question(negated_condition: str, inner_text: str) -> str:
    return "\n".join([
        f'if {negated_condition} {{',
        indent(inner_text, "\t"),
        f'}}'
    ])


def get_final_failed_statement(root: Node) -> str:
    final_failed_statement = f'"Property {root.to_question()} does not holds" result: bool(true)'
    return "\n".join([
        f'if {root_to_failed_statement(root)} {{',
        indent(final_failed_statement, "\t"),
        f'}}'
    ])


def get_question_from_branch(branch: set[ALL_NODE_TYPES], node_to_type_map: dict[str, str]) -> str:
    return "\n".join([leaf_to_question(leaf, node_to_type_map) for leaf in branch_to_leaves(branch)])


def consume_branches(root: Node, branches: list[set[ALL_NODE_TYPES]], node_to_type_map: dict[str, str]) -> str:
    if not branches:
        return ""
    current_branch = branches[0]
    return "\n".join([
        f'{get_question_from_branch(current_branch, node_to_type_map)}',
        f'{get_if_success_holds(root, branch_to_success_condition(current_branch))}',
        f'{get_if_negated_go_to_next_set_of_question(branch_to_negated_condition(current_branch), consume_branches(root, branches[1:], node_to_type_map)) if len(branches) > 1 else get_final_failed_statement(root)}',
    ])
