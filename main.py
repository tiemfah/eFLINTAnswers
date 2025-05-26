from algorithms.branch_to_leaves import branch_to_leaves
from algorithms.branch_to_negated_condition import branch_to_negated_condition
from algorithms.branch_to_success_condition import branch_to_success_condition
from algorithms.leaf_to_question import leaf_to_question
from algorithms.root_to_branches import root_to_branches
from algorithms.root_to_failed_statement import root_to_failed_statement
from eflint_lib import EF
from eflint_parser import create_graph, get_node_to_type_map

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

    """
    algorithm map-to-LiveQL 
        input: root
        output: LiveQL DSL string
    
        branches <- call root-to-branches with root
        branches <- call ascending sort branches with size as key
        
        liveql <- empty string
        for each branch in branches do
            
            leaves <- call branch-to-leaves with branches
            for each leaf in leaves do
                question-line <- call leaf-to-question with leaf
                add liveql with question-line
            
            success-condition <- call branch-to-success-condition with branch
            add liveql with success-condition
            
            negated-condition <- call branch-to-negated-condition with branch
            add liveql with negated-condition

        root-failed-statement <- call root-to-failed-statement with root
        add liveql with root-to-failed-statement
    """
    graph = create_graph(type_res)
    human_node = graph["human"]

    branches = root_to_branches(human_node)
    branches = sorted(branches, key=len)
    for branch in branches:
        for leaf in branch_to_leaves(branch):
            print(leaf_to_question(leaf, node_to_type_map))
        print(branch_to_success_condition(branch))
        print(branch_to_negated_condition(branch))
    print(root_to_failed_statement(human_node))

"""
"Is the actor intelligent?" intelligent: bool
"Is the actor not intelligent?" not_intelligent: bool
if (intelligent) {
    "Property human holds" result: bool(true)"
}
if (not_intelligent) {
    "Is the actor featherless?" featherless: bool
    "Is the actor not featherless?" not_featherless: bool
    
    "How many number of legs does the actor have?": number_of_legs: int
}
if (featherless && number_of_legs == 2) {
    "Property human holds" result: bool(true)"
}
if (not_intelligent && (not_featherless || number_of_legs != 2)) {
    "Property human does not holds" result: bool(true)"
}
"""
