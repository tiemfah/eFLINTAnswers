from model import *


def branch_to_success_condition(branch: set[ALL_NODE_TYPES]) -> str:
    """
    algorithm branch-to-success-condition is
        input: set of Node
        output: string representing the success condition

        for example:
            Node(A) -> Node(B) -> AndNode(Node(D), Node(C)) should return (D && C)

        root <- get root from node in set of node, root is the one without any dependee.

        algorithm collect-success-condition is
            input: set of Node
            input: root of the set of nodes
            output: string representing the success condition

            if root does not have any dependee, return empty string.
            else do
                root-type <- call type-of-root with root
                children <- node.dependencies filter with dependency in given set of Node
                if children is empty then return empty string.
                else case root-type of
                    AndNode : do
                        children-condition <- call collect-success-condition with child in children
                        return call join children-condition with " && "
                    OrNode : do
                        children-condition <- call collect-success-condition with child in children
                        return call join children-condition with " || "
                    EqualNode : do
                     ....

        return call collect-success-condition with root
    """
    if not branch:
        return ""

    # Find the root node (no other node in branch depends on it)
    roots = [n for n in branch if not any(n in getattr(dep, "dependencies", []) for dep in branch)]

    if not roots:
        # Handle circular dependencies - pick any node as root
        return f"({getattr(next(iter(branch)), 'name', str(next(iter(branch))))})"

    def collect_success(node, visited_branch):
        if hasattr(node, "dependencies") and node.dependencies:
            children = [dep for dep in node.dependencies if dep in visited_branch]

            if not children:
                return node.to_liveql_var()

            elif isinstance(node, NotNode):
                child_conditions = [collect_success(child, visited_branch) for child in children]
                return f"!({"".join(child_conditions)})"

            elif isinstance(node, EqualsNode):
                return f"{node.left.to_liveql_var()} == {node.right.to_live_ql_value()}"

            elif isinstance(node, LesserNode):
                return f"{node.left.to_liveql_var()} < {node.right.to_liveql_var()}"

            elif isinstance(node, LesserOrEqualNode):
                return f"{node.left.to_liveql_var()} <= {node.right.to_liveql_var()}"

            elif isinstance(node, GreaterNode):
                return f"{node.left.to_liveql_var()} > {node.right.to_liveql_var()}"

            elif isinstance(node, GreaterOrEqualNode):
                return f"{node.left.to_liveql_var()} >= {node.right.to_liveql_var()}"

            elif isinstance(node, AndNode):
                child_conditions = [collect_success(child, visited_branch) for child in children]
                return " && ".join(child_conditions)

            elif isinstance(node, OrNode):
                child_conditions = [collect_success(child, visited_branch) for child in children]
                return " || ".join(child_conditions)

            else:
                return collect_success(children[0], visited_branch)

        return node.to_liveql_var()

    if len(roots) > 1:
        root_conditions = [collect_success(root, branch) for root in roots]
        return f"({' && '.join(root_conditions)})"

    root = roots[0]

    return f"({collect_success(root, branch)})"
