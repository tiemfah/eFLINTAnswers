#
# def node_to_string(root: ALL_NODE_TYPES) -> str:
#     """
#     Convert a Node graph into a string representation of a logical expression.
#
#     Examples:
#     - "bool(intelligent || (featherless && number_of_legs == 2))"
#
#     Args:
#         root: The root node of the graph
#
#     Returns:
#         A string representation of the logical expression
#     """
#     # Keep track of visited nodes to avoid cycles
#     visited = set()
#
#     def process_node(node):
#         # Avoid cycles by tracking visited nodes by their identity
#         node_id = id(node)
#         if node_id in visited:
#             return node.name  # Return just the name to avoid infinite recursion
#
#         visited.add(node_id)
#
#         if isinstance(node, OrNode):
#             # Get all dependencies and join them with OR operator
#             deps = [process_node(dep) for dep in node.dependencies]
#             deps_str = " || ".join(deps)
#             return deps_str
#
#         elif isinstance(node, AndNode):
#             # Get all dependencies and join them with AND operator
#             deps = [process_node(dep) for dep in node.dependencies]
#             deps_str = " && ".join(deps)
#             return deps_str
#
#         elif isinstance(node, EqualsNode):
#             # Process equals operator with left and right sides
#             left = process_node(node.left) if node.left else ""
#             right = process_node(node.right) if node.right else ""
#             return f"{left} == {right}"
#
#         elif isinstance(node, Node):
#             # For a regular node:
#             # 1. If it has dependencies, process them
#             if node.dependencies:
#                 # This is a node that leads to other nodes in the graph
#                 # Instead of returning its name, we need to process its dependencies
#                 # This is likely where the original function went wrong
#                 if len(node.dependencies) == 1:
#                     # If there's only one dependency, just return that result
#                     return process_node(node.dependencies[0])
#                 else:
#                     # Multiple dependencies - would need to define how these combine
#                     # For now, assuming they combine with AND
#                     deps = [process_node(dep) for dep in node.dependencies]
#                     return " && ".join(deps)
#             else:
#                 # It's a leaf node, just return its name
#                 return node.name
#
#         # Handle edge cases
#         return ""
#
#     # Start with the root node and wrap in bool()
#     result_string = process_node(root)
#
#     # Add parentheses for complex expressions
#     if " || " in result_string or " && " in result_string:
#         if not (result_string.startswith("(") and result_string.endswith(")")):
#             # Add parentheses for proper grouping in complex expressions
#             parts = result_string.split(" || ")
#             for i, part in enumerate(parts):
#                 if " && " in part and not (part.startswith("(") and part.endswith(")")):
#                     parts[i] = f"({part})"
#             result_string = " || ".join(parts)
#
#     return f"({result_string})"


# def generate_dsl(root: Node, node_to_type: Dict[str, str], set_of_questions: Set[ALL_NODE_TYPES]) -> str:
#     # leaf_nodes = collect_leaf_nodes(root)
#     leaf_nodes = []
#     lines = [f"form {root.name} {{"]
#     for name in sorted(leaf_nodes):
#         node_type = node_to_type.get(name, 'string')  # Default to string if type not found
#
#         # Format name for question by replacing underscores with spaces
#         formatted_name = name.replace("_", " ")
#
#         # Customize question based on the type
#         if node_type == 'bool':
#             question = f'"Is the actor {formatted_name}?"'
#         elif node_type == 'int':
#             question = f'"How many {formatted_name} does the actor have?"'
#         elif node_type == 'string':
#             question = f'"What is the actor {formatted_name}?"'
#         else:
#             # Generic fallback for any other types
#             question = f'"Enter your {formatted_name}:"'
#
#         lines.append(f"  {question}")
#         lines.append(f"     {name}: {node_type}")
#
#     # Add the logical expression from the root node
#     lines.append(f"  if {node_to_string(root)} " + "{")
#     lines.append(f"    \"Property {root.name} holds\" result: bool(true)")
#     lines.append("  } else {")
#     lines.append(f"    \"Property {root.name} does not holds\" result: bool(true)")
#     lines.append("  }")
#     lines.append("}")
#
#     return "\n".join(lines)
