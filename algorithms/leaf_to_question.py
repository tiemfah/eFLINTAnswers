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
    formatted_name = node.to_question()
    formatted_var_name = node.to_liveql_var()
    match node_to_type_map.get(node.name, ""):
        case "int":
            return f'"How many {formatted_name} does the actor have?" {formatted_var_name}: {node_to_type_map[node.name]}'
        case "bool":
            return f'"Is the actor {formatted_name}?" {formatted_var_name}: bool\n"Is the actor not {formatted_name}?" not_{formatted_var_name}: bool'
        case "string":
            return f'"What is the actor {formatted_name}?" {formatted_var_name}: {node_to_type_map[node.name]}'
        case _:
            # raise Exception(f"Unknown node type: {type(node)} of value: {node}")
            return f'"Is the actor {formatted_name}?" {formatted_var_name}: bool\n"Is the actor not {formatted_name}?" not_{formatted_var_name}: bool'
