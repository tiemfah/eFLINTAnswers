from algorithms.root_to_liveql import root_to_liveql
from eflint.eflint_lib import EF
from eflint.eflint_parser import create_graph, get_node_to_type_map, get_parameter_facts
from graph_visualizer import visualize_graph

from eflint.save_and_open import save_dsl_to_file, open_liveql

if __name__ == '__main__':
    """
    algorithm parse-term-to-node is
    
        input: terms JSON
        output: Node
        
        recursively parse the term, each term will have term-type. each term-type have to be handled manually.
        
        for each term in terms do
            node <- term
            for each sub-term in sub-terms do
                add node.dependency with call parse-term-to-node with sub-term
    
    algorithm parse-eflint-to-node is
    
        input: type_response JSON
        output: map of type to node
        
        parse all type in types
        
        type-to-node <- {}
        for each type in type_response do
            for each derivation in type.derivations do
                type-to-node with key of type <- call parse-term-to-node with derivation.term 
    """
    ef = EF()
    type_res = ef.types()
    fact_res = ef.facts()
    node_name_to_node = create_graph(type_res)
    node_to_type_map = get_node_to_type_map(type_res)
    parameter_facts = get_parameter_facts(type_res, fact_res)
    root = node_name_to_node['[Recht op IIT 231]']
    # visualize_graph(root)
    dsl_content = root_to_liveql(root, node_to_type_map, parameter_facts)
    # print(dsl_content)
    # print(node_to_type_map)
    save_dsl_to_file(dsl_content, "human", "/Users/tiemfah/Projects/LiveQL/bin/nl/cwi/swat/liveql/examples/eflint.ql")
    open_liveql()
