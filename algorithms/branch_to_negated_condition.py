from model import *


def branch_to_negated_condition(branch: set[ALL_NODE_TYPES]) -> str:
    """
    A branch represents a possible path leading to the root property holding.
    This is for triggering next branch of question
    :param branch:
    :return:
    """
    # Find all leaf nodes (nodes with no dependencies in the branch)
    leaves = [node for node in branch if not any(dep in branch for dep in getattr(node, "dependencies", []))]
    # Negate their names
    negated = [f"not_{getattr(node, 'name', '')}" for node in leaves]
    # Join with ||
    return f"({' || '.join(negated)})" if negated else ""