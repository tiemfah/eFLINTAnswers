from model import Node


def leaf_to_question(node: Node, node_to_type_map: dict[str, str]) -> str:
    """
    algorithm leaf-to-question is
    input: node: Node
    input: node_to_type_map: dict[node, primitive-type]
    :return: string

    case primitive-type from node_to_type_map with node of
        int: return int wording
        ....
    end case
    """
    formatted_name = node.name.replace("_", " ")
    match node_to_type_map.get(node.name, ""):
        case "int":
            return f'"How many {formatted_name} does the actor have?" {node.name}: {node_to_type_map[node.name]}'
        case "bool":
            return f'"Is the actor {formatted_name}?" {node.name}: bool\n"Is the actor not {formatted_name}?" not_{node.name}: bool'
        case "string":
            return f'"What is the actor {formatted_name}?" {node.name}: {node_to_type_map[node.name]}'
        case _:
            raise Exception(f"Unknown node type: {type(node)}")
