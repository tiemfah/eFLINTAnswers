from model import *


def branch_to_negated_condition(branch: set[ALL_NODE_TYPES]) -> str:
    """
    Returns the negated condition for a branch, reversing the logic of branch_to_success_condition.
    For example, if the success condition is (A && (B || C)), the negated condition is (not_A || (not_B && not_C)).
    """
    if not branch:
        return ""

    # Find the root node (no other node in branch depends on it)
    roots = [n for n in branch if not any(n in getattr(dep, "dependencies", []) for dep in branch)]

    def collect_negated(node, visited_branch):
        if hasattr(node, "dependencies") and node.dependencies:
            children = [dep for dep in node.dependencies if dep in visited_branch]

            if not children:
                return f"not_{getattr(node, 'name', str(node))}"

            elif isinstance(node, (EqualsNode, LesserNode, LesserOrEqualNode, GreaterNode, GreaterOrEqualNode)):
                left = node.left
                right = node.right
                return f"{left.name} != {right.name}"

            elif isinstance(node, AndNode):
                child_conditions = [collect_negated(child, visited_branch) for child in children]
                return " || ".join(child_conditions)

            elif isinstance(node, OrNode):
                child_conditions = [collect_negated(child, visited_branch) for child in children]
                return " && ".join(child_conditions)

            else:
                return collect_negated(children[0], visited_branch)

        return f"not_{getattr(node, 'name', str(node))}"

    if not roots:
        # Handle circular dependencies - pick any node as root
        return f"(not_{getattr(next(iter(branch)), 'name', str(next(iter(branch))))})"

    if len(roots) > 1:
        root_conditions = [collect_negated(root, branch) for root in roots]
        return f"({' || '.join(root_conditions)})"

    root = roots[0]
    return f"({collect_negated(root, branch)})"
