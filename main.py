from algorithms.root_to_liveql import root_to_liveql
from eflint.eflint_lib import EF
from eflint.eflint_parser import create_graph, get_node_to_type_map
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
    ef.phrase("Fact entity Identified by String")
    ef.phrase("Fact number_of_legs Identified by entity * int")
    ef.phrase("Fact featherless Identified by entity")
    ef.phrase("Fact biped Identified by entity Holds when (Exists number_of_legs : number_of_legs(entity, 2))")
    ef.phrase("Fact intelligent Identified by entity")  # this is the new one
    ef.phrase(
        "Fact human Identified by entity Holds when (biped(entity) && featherless(entity)) || intelligent(entity)")

    type_res = ef.types()
    node_to_type_map = get_node_to_type_map(type_res)
    graph = create_graph(type_res)
    human_node = graph["human"]

    dsl_content = root_to_liveql(human_node, node_to_type_map)
    # save_dsl_to_file(dsl_content, "human", "/Users/tiemfah/Projects/LiveQL/bin/nl/cwi/swat/liveql/examples/eflint.ql")
    # open_liveql()
