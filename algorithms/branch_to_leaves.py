from model import ALL_NODE_TYPES


def branch_to_leaves(branch: set[ALL_NODE_TYPES]) -> set[ALL_NODE_TYPES]:
    leaves = set()
    for node in branch:
        if not node.dependencies:
            leaves.add(node)
    return leaves
