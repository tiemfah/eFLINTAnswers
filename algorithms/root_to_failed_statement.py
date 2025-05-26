from model import *


def root_to_failed_statement(root: Node) -> str:
    def helper(node):
        if isinstance(node, Node) and not node.dependencies:
            return f"not_{node.name}"
        if isinstance(node, AndNode):
            return "(" + " || ".join(helper(dep) for dep in node.dependencies) + ")"
        if isinstance(node, OrNode):
            return "(" + " && ".join(helper(dep) for dep in node.dependencies) + ")"
        # Traverse to the next dependency if it's a plain Node
        if isinstance(node, Node) and node.dependencies:
            return helper(node.dependencies[0])
        return ""

    return helper(root)
