from dataclasses import dataclass
from typing import Union, List

ALL_NODE_TYPES = Union["Node", "IntNode", "BoolNode", "StringNode", "OrNode", "AndNode", "EqualsNode", "GreaterNode"]


@dataclass
class Node:
    name: str
    dependencies: List[ALL_NODE_TYPES] = None

    def __repr__(self):
        return f"{self.name} -> ({", ".join([dep.name for dep in self.dependencies]) if self.dependencies else "None"})"

    def __post_init__(self):
        if self.dependencies is None:
            self.dependencies = []

    def __hash__(self):
        return id(self)

    def __eq__(self, other):
        return hash(self) == hash(other)

    def to_liveql_var(self):
        return str(self.name).replace(" ", "_").replace("[", "").replace("]", "")

    def to_question(self):
        return str(self.name).replace("_", " ").replace("[", "").replace("]", "")


@dataclass(eq=False)
class OrNode(Node):
    name: str = "OR"

    def __repr__(self):
        return f"{self.name} -> ({", ".join([dep.name for dep in self.dependencies]) if self.dependencies else "None"})"


@dataclass(eq=False)
class AndNode(Node):
    name: str = "AND"

    def __repr__(self):
        return f"{self.name} -> ({", ".join([dep.name for dep in self.dependencies]) if self.dependencies else "None"})"


@dataclass(eq=False)
class NotNode(Node):
    name: str = "NOT"

    def __repr__(self):
        return f"{self.name} -> ({", ".join([dep.name for dep in self.dependencies]) if self.dependencies else "None"})"


@dataclass(eq=False)
class CountNode(Node):
    name: str = "COUNT"


@dataclass(eq=False)
class EqualsNode(Node):
    name: str = "EQUALS"
    left: Node = None
    right: Node = None

    def __repr__(self):
        return f"{type(self).__name__} -> (left={self.left.name}, right={self.right.name})"


@dataclass(eq=False)
class GreaterNode(Node):
    name: str = "GREATER"
    left: Node = None
    right: Node = None

    def __repr__(self):
        return f"{type(self).__name__} -> (left={self.left.name}, right={self.right.name})"


@dataclass(eq=False)
class GreaterOrEqualNode(Node):
    name: str = "GREATER_OR_EQUAL"
    left: Node = None
    right: Node = None

    def __repr__(self):
        return f"{type(self).__name__} -> (left={self.left.name}, right={self.right.name})"


@dataclass(eq=False)
class LesserNode(Node):
    name: str = "LESSER"
    left: Node = None
    right: Node = None

    def __repr__(self):
        return f"{type(self).__name__} -> (left={self.left.name}, right={self.right.name})"


@dataclass(eq=False)
class LesserOrEqualNode(Node):
    name: str = "LESSER_OR_EQUAL"
    left: Node = None
    right: Node = None

    def __repr__(self):
        return f"{type(self).__name__} -> (left={self.left.name}, right={self.right.name})"
