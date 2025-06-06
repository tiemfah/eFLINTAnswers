from typing import Dict, Optional, Any

from model import *


class TermParser:
    """Handles parsing of term structures into nodes"""

    def __init__(self, type_response: dict, node_cache: Dict[str, Node]):
        self.type_response = type_response
        self.node_cache = node_cache

    def parse_term(self, term: Dict) -> List[ALL_NODE_TYPES]:
        """Parse a term structure and return corresponding nodes"""
        term_type = term.get("term-type")
        if not term_type:
            return []

        parser_method = getattr(self, f'_parse_{term_type.lower()}', None)
        if parser_method:
            return parser_method(term)

        return []

    def _parse_when(self, term: Dict) -> List[ALL_NODE_TYPES]:
        parent_node_name = term["t1"]["var"]["domID"]
        dependency_node = self.parse_term(term["t2"])
        self.node_cache[parent_node_name].dependencies.extend(dependency_node)

        return [dependency_node]

    def _parse_and(self, term: Dict) -> List[ALL_NODE_TYPES]:
        """Parse AND term"""
        and_node = AndNode()

        for sub_term_key in ["t1", "t2"]:
            sub_term = term.get(sub_term_key, {})
            sub_dependencies = self.parse_term(sub_term)
            and_node.dependencies.extend(sub_dependencies)

        return [and_node] if and_node.dependencies else []

    def _parse_or(self, term: Dict) -> List[ALL_NODE_TYPES]:
        """Parse OR term"""
        or_node = OrNode()

        for sub_term_key in ["t1", "t2"]:
            sub_term = term.get(sub_term_key, {})
            sub_dependencies = self.parse_term(sub_term)
            or_node.dependencies.extend(sub_dependencies)

        return [or_node] if or_node.dependencies else []

    def _parse_present(self, term: Dict) -> List[ALL_NODE_TYPES]:
        """Parse Present term"""
        equals_node = self._try_parse_equality_utrecht(term)
        if equals_node:
            return [equals_node]
        sub_term = term.get("t", {})
        return self.parse_term(sub_term)

    def _parse_exists(self, term: Dict) -> List[ALL_NODE_TYPES]:
        """Parse Exists term"""
        equals_node = self._try_parse_equality(term)
        if equals_node:
            return [equals_node]

        # Fallback to parsing the nested term
        sub_term = term.get("t", {})
        return self.parse_term(sub_term)

    def _parse_eq(self, term: Dict) -> List[ALL_NODE_TYPES]:
        """Parse Equality term"""
        equals_node = EqualsNode()
        left = self.parse_term(term.get("t1", {}))[0]
        equals_node.left = left
        right = self._parse_tag(term.get("t2", {}))[0]
        equals_node.right = right
        equals_node.dependencies.extend([left, right])
        return [equals_node] if equals_node.dependencies else []

    def _parse_intlit(self, term: Dict) -> List[ALL_NODE_TYPES]:
        """Parse Intlit term"""
        return [Node(term["int"])]

    def _parse_count(self, term: Dict) -> List[ALL_NODE_TYPES]:
        """Parse Count term"""
        count_node = CountNode()

        count_vars = term.get("vars", [])
        for var in count_vars:
            count_node.dependencies.append(Node(var["domID"]))

        return [count_node]

    def _parse_ge(self, term: Dict) -> List[ALL_NODE_TYPES]:
        """Parse Ge term"""
        greater_than_node = GreaterNode()

        for sub_term_key in ["t1", "t2"]:
            sub_term = term.get(sub_term_key, {})
            sub_dependencies = self.parse_term(sub_term)
            greater_than_node.dependencies.extend(sub_dependencies)

        if len(greater_than_node.dependencies) == 2:
            greater_than_node.left = greater_than_node.dependencies[0]
            greater_than_node.right = greater_than_node.dependencies[1]

        return [greater_than_node] if greater_than_node.dependencies else []

    def _parse_geq(self, term: Dict) -> List[ALL_NODE_TYPES]:
        """Parse Geq term"""
        greater_or_equal_node = GreaterOrEqualNode()

        for sub_term_key in ["t1", "t2"]:
            sub_term = term.get(sub_term_key, {})
            sub_dependencies = self.parse_term(sub_term)
            greater_or_equal_node.dependencies.extend(sub_dependencies)

        if len(greater_or_equal_node.dependencies) == 2:
            greater_or_equal_node.left = greater_or_equal_node.dependencies[0]
            greater_or_equal_node.right = greater_or_equal_node.dependencies[1]

        return [greater_or_equal_node] if greater_or_equal_node.dependencies else []

    def _parse_le(self, term: Dict) -> List[ALL_NODE_TYPES]:
        """Parse Le term"""
        lesser_node = LesserNode()

        for sub_term_key in ["t1", "t2"]:
            sub_term = term.get(sub_term_key, {})
            sub_dependencies = self.parse_term(sub_term)
            lesser_node.dependencies.extend(sub_dependencies)

        if len(lesser_node.dependencies) == 2:
            lesser_node.left = lesser_node.dependencies[0]
            lesser_node.right = lesser_node.dependencies[1]

        return [lesser_node] if lesser_node.dependencies else []

    def _parse_leq(self, term: Dict) -> List[ALL_NODE_TYPES]:
        """Parse Leq term"""
        lesser_or_equal_node = LesserOrEqualNode()

        for sub_term_key in ["t1", "t2"]:
            sub_term = term.get(sub_term_key, {})
            sub_dependencies = self.parse_term(sub_term)
            lesser_or_equal_node.dependencies.extend(sub_dependencies)

        if len(lesser_or_equal_node.dependencies) == 2:
            lesser_or_equal_node.left = lesser_or_equal_node.dependencies[0]
            lesser_or_equal_node.right = lesser_or_equal_node.dependencies[1]

        return [lesser_or_equal_node] if lesser_or_equal_node.dependencies else []

    def _parse_app(self, term: Dict) -> List[ALL_NODE_TYPES]:
        """Parse App term"""
        dom_id = term.get("domID")
        if dom_id and dom_id in self.type_response["types"]:
            return self._extract_dependencies(dom_id)
        return []

    def _parse_ref(self, term: Dict) -> List[ALL_NODE_TYPES]:
        """Parse Ref term"""
        dom_id = term.get("var", {}).get("domID", '')
        if dom_id and dom_id in self.type_response["types"]:
            return self._extract_dependencies(dom_id)
        return []

    def _parse_tag(self, term: Dict) -> List[ALL_NODE_TYPES]:
        """Parse Tag term"""
        if term.get("t", {}).get("term-type", {}) == "StringLit":
            return [Node(name=term.get("t", {}).get("string", ""))]
        else:
            raise Exception(f"Unknown term type: {term.get('term-type')}")

    def _parse_untag(self, term: Dict) -> List[ALL_NODE_TYPES]:
        """Parse Untag term -> skipping it."""
        return self.parse_term(term.get("t", {}))

    def _parse_not(self, term: Dict) -> List[ALL_NODE_TYPES]:
        """Parse Not term"""
        not_node = NotNode()
        sub_term = term.get("t", {})
        sub_dependencies = self.parse_term(sub_term)
        not_node.dependencies.extend(sub_dependencies)
        return [not_node] if not_node.dependencies else []

    def _try_parse_equality(self, term: Dict) -> Optional[EqualsNode]:
        """Try to parse an equality expression from an Exists term"""
        present_term = term.get("t", {})

        if not self._is_present_term(present_term):
            return None

        inner_term = present_term.get("t", {})
        if not self._is_app_term(inner_term):
            return None

        left_value = inner_term.get("domID", '')
        right_value = self._extract_int_value(inner_term)

        if left_value and right_value is not None:
            return self._create_equality_node(left_value, right_value)

        return None

    def _try_parse_equality_utrecht(self, term: Dict) -> Optional[EqualsNode]:
        """Try to parse an equality expression for [Tag] == 'StringLit'"""
        if not self._is_present_term(term):
            return None

        tag_term = term.get("t", {})
        if tag_term.get("term-type") == "Tag":
            dom_id = tag_term.get("domID")
            string_lit = tag_term.get("t", {})
            if string_lit.get("term-type") == "StringLit":
                left_node = Node(name=dom_id)
                right_node = Node(name=string_lit.get("string", ""))
                return EqualsNode(
                    name=f"{dom_id} == {string_lit.get('string', '')}",
                    dependencies=[left_node, right_node],
                    left=left_node,
                    right=right_node
                )
        return None

    def _is_present_term(self, term: Dict) -> bool:
        """Check if term is a Present term"""
        return term.get("term-type") == 'Present'

    def _is_app_term(self, term: Dict) -> bool:
        """Check if term is an App term"""
        return term.get("term-type") == 'App'

    def _extract_int_value(self, app_term: Dict) -> Optional[int]:
        """Extract integer value from App term arguments"""
        args = app_term.get("args", {}).get('Right', [])

        for arg in args:
            term_obj = arg.get('term', {})
            if self._is_int_tag(term_obj):
                int_lit = term_obj.get('t', {})
                if int_lit.get('term-type') == 'IntLit':
                    return int_lit.get('int')

        return None

    def _is_int_tag(self, term_obj: Dict) -> bool:
        """Check if term object is an int tag"""
        return (term_obj.get('term-type') == 'Tag' and
                term_obj.get('domID') == 'int')

    def _create_equality_node(self, left_value: str, right_value: int) -> EqualsNode:
        """Create an equality node with left and right operands"""
        left_node = Node(name=left_value)
        right_node = Node(name=str(right_value))

        return EqualsNode(
            name=f"{left_value} == {right_value}",
            dependencies=[left_node, right_node],
            left=left_node,
            right=right_node
        )

    def _extract_dependencies(self, node_name: str) -> List[ALL_NODE_TYPES]:
        """Extract dependencies for a given node name"""
        if node_name not in self.type_response["types"]:
            return []

        if node_name in self.node_cache:
            return [self.node_cache[node_name]]

        node = Node(name=node_name)
        self.node_cache[node_name] = node

        dependencies = self._get_node_dependencies(node_name)
        node.dependencies = dependencies

        return [node]

    def _get_node_dependencies(self, node_name: str) -> List[ALL_NODE_TYPES]:
        """Get dependencies for a specific node"""
        type_definition = self.type_response["types"][node_name]

        if not self._has_derivations(type_definition):
            return []

        dependencies = []
        for derivation in type_definition["derivation"]:
            if derivation.get("derivation-type") == 'HoldsWhen':
                term = derivation.get("term")
                if term:
                    dependencies.append(self.parse_term(term))

        # Flatten and join with OrNode if there are multiple dependencies
        flat_dependencies = [item for sublist in dependencies for item in sublist]
        if len(flat_dependencies) > 1:
            or_node = OrNode()
            or_node.dependencies.extend(flat_dependencies)
            flat_dependencies = [or_node]

        if type_definition["kind"]["kind-type"] == 'Act':
            for effect in type_definition["kind"]["act"]["effects"]:
                if effect.get("effect-type") == 'CAll':
                    if effect.get("vars", []):
                        effect_deps = self.parse_term(effect.get("term"))
                        if flat_dependencies:
                            # Combine with existing OrNode if present
                            if isinstance(flat_dependencies[0], OrNode):
                                flat_dependencies[0].dependencies.extend(effect_deps)
                            else:
                                or_node = OrNode()
                                or_node.dependencies.extend(flat_dependencies + effect_deps)
                                flat_dependencies = [or_node]
                        else:
                            flat_dependencies = effect_deps

        return flat_dependencies

    def _has_derivations(self, type_definition: Dict) -> bool:
        """Check if type definition has derivations"""
        return ("derivation" in type_definition and
                type_definition["derivation"])


class GraphCreator:
    """Main class for creating graphs from types response"""

    def __init__(self, type_response: dict):
        self.type_response = type_response
        self.node_cache: Dict[str, Node] = {}
        self.term_parser = TermParser(type_response, self.node_cache)

    def create_graph(self) -> Dict[str, Node]:
        """
        Convert a response types json to a graph that is connected then return
        the dict of query to root node of that query.
        """
        self._process_all_types()
        return self.node_cache.copy()

    def _process_all_types(self) -> None:
        """Process all types in the response"""
        for type_name in self.type_response["types"]:
            if type_name not in self.node_cache:
                self.term_parser._extract_dependencies(type_name)


def create_graph(type_res: dict) -> Dict[str, Node]:
    """
    Convert a response types json to a graph that is connected then return
    the dict of query to root node of that query.

    Args:
        type_res: Dictionary containing types response data

    Returns:
        Dictionary mapping type names to their corresponding root nodes
    """
    creator = GraphCreator(type_res)
    return creator.create_graph()


def get_node_to_type_map(type_res: dict) -> Dict[str, str]:
    """
    THIS ONE COULD ONLY HANDLE PRODUCTS OF 2 TYPE

    Infers types from domain structures and returns a dictionary mapping node names to types.

    Args:
        type_res: Dictionary containing the 'types' key with node definitions

    Returns:
        Dictionary mapping node names to their inferred types
    """
    type_map = {}
    types_data = type_res.get('types', {})

    for node_name, node_info in types_data.items():
        if 'domain' in node_info:
            domain = node_info['domain']
            domain_type = domain.get('domain-type')

            if domain_type == 'AnyString' or domain_type == 'String' or domain_type == 'Strings':
                type_map[node_name] = 'str'
            elif domain_type == 'AnyInt' or domain_type == 'Ints':
                type_map[node_name] = 'int'
            elif domain_type == 'Products':
                vars_list = domain.get('vars', [])
                if len(vars_list) == 1:
                    type_map[node_name] = 'bool'
                elif len(vars_list) == 2:
                    dom_ids = [var.get('domID') for var in vars_list]
                    if 'entity' in dom_ids and 'int' in dom_ids:
                        type_map[node_name] = 'int'

    return type_map


def get_parameter_facts(type_res: dict[str: Any], fact_res: dict[str: Any]) -> Dict[str, Any]:
    facts = {}
    for type_name, type_value in type_res["types"].items():
        if type_value["kind"]["kind-type"] == 'Fact':
            facts[type_name] = None
    for fact in fact_res["values"]:
        if fact["fact-type"] in facts:
            facts[fact["fact-type"]] = fact["value"]
    return {k.replace("[", "").replace("]", ""): v for k, v in facts.items() if v is not None}
