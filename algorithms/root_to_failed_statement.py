from model import *


def root_to_failed_statement(root: Node) -> str:
    def helper(node):
        if isinstance(node, Node) and not node.dependencies:
            return f"not_{node.to_liveql_var()}"

        elif isinstance(node, NotNode):
            child_conditions = [helper(dep) for dep in node.dependencies]
            return f"!({"".join(child_conditions)})"

        elif isinstance(node, EqualsNode):
            return f"{node.left.to_liveql_var()} != {node.right.to_live_ql_value()}"

        elif isinstance(node, LesserNode):
            return f"{node.left.to_liveql_var()} >= {node.right.to_liveql_var()}"

        elif isinstance(node, LesserOrEqualNode):
            return f"{node.left.to_liveql_var()} > {node.right.to_liveql_var()}"

        elif isinstance(node, GreaterNode):
            return f"{node.left.to_liveql_var()} <= {node.right.to_liveql_var()}"

        elif isinstance(node, GreaterOrEqualNode):
            return f"{node.left.to_liveql_var()} < {node.right.to_liveql_var()}"

        if isinstance(node, AndNode):
            return "(" + " || ".join(helper(dep) for dep in node.dependencies) + ")"

        if isinstance(node, OrNode):
            return "(" + " && ".join(helper(dep) for dep in node.dependencies) + ")"

        # Traverse to the next dependency if it's a plain Node
        if isinstance(node, Node) and node.dependencies:
            return helper(node.dependencies[0])
        return ""

    return helper(root)
