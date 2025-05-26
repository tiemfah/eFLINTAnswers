from model import *


def root_to_branches(root: Node) -> list[set[ALL_NODE_TYPES]]:
    """
    algorithm root-to-branches is
        input: root Node
        output: set of all branches

        use dfs to traverse branches, and split out if OrNode is found

        do dfs on node
            if node is leaf
                do return node
            else if node is OrNode
                do split the current branch into separate branches for each dependency including current node
            else if node is EqualNode
                do call dfs with node.left
            else if node is AndNode
                do compute cartesian product of all branches and union them with current node
            else
                do call dfs with each dependency in node.dependencies
        call dfs with root
    """
    def dfs(node):
        if isinstance(node, EqualsNode):
            return [dfs(node.left)]
        if not node.dependencies:
            return [{node}]
        if isinstance(node, OrNode):
            return [{node} | branch for dep in node.dependencies for branch in dfs(dep)]
        if isinstance(node, AndNode):
            from itertools import product
            dep_branches = [dfs(dep) for dep in node.dependencies]
            return [{node} | set().union(*combo) for combo in product(*dep_branches)]
        return [{node} | branch for dep in node.dependencies for branch in dfs(dep)]

    return dfs(root)
