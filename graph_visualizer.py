import matplotlib.pyplot as plt
import networkx as nx

from model import ALL_NODE_TYPES, Node, OrNode, AndNode, EqualsNode


def visualize_graph_prime(node: ALL_NODE_TYPES, fig_size=(12, 9), title=None):
    """
    Visualize a Node and its dependencies as a network graph using NetworkX and Matplotlib.
    Properly handles AndNode and OrNode types.
    """
    # Create directed graph
    graph = nx.DiGraph()

    # Keep track of visited nodes to avoid cycles
    visited = set()

    root_node = node

    # Add nodes and edges recursively
    def add_nodes_and_edges(n, parent=None):
        if isinstance(n, EqualsNode):
            node_label = "EXISTS"
            node_color = 'lightyellow'
        elif isinstance(n, AndNode):
            node_label = "AND"
            node_color = 'lightgreen'
        elif isinstance(n, OrNode):
            node_label = "OR"
            node_color = 'salmon'
        elif isinstance(n, Node):
            node_label = n.name
            node_color = 'lightblue'
            if id(n) == id(root_node):
                node_color = 'pink'
        else:
            return

        # Add the node with its attributes
        graph.add_node(id(n), label=node_label, color=node_color)

        # Add edge from parent if it exists
        if parent:
            graph.add_edge(parent, id(n))

        # Skip if we've already processed this Node to avoid cycles
        if isinstance(n, Node) and n.name in visited:
            return

        # Mark as visited
        if isinstance(n, Node):
            visited.add(n.name)

        # Process dependencies
        for dep in n.dependencies:
            add_nodes_and_edges(dep, id(n))

        if isinstance(n, EqualsNode):
            add_nodes_and_edges(n.left, id(n))
            add_nodes_and_edges(n.right, id(n))

    # Start with the main node
    add_nodes_and_edges(node)

    # Extract node attributes
    node_colors = [graph.nodes[n].get('color', 'white') for n in graph.nodes()]
    node_labels = {n: graph.nodes[n].get('label', n) for n in graph.nodes()}

    # Create figure
    plt.figure(figsize=fig_size)
    if title:
        plt.title(title)

    # Set node positions
    pos = nx.spring_layout(graph, seed=42, k=0.5)

    # Draw nodes
    nx.draw(graph, pos,
            labels=node_labels,
            node_color=node_colors,
            edgecolors='black',
            node_size=2000,
            font_size=10,
            font_weight='bold',
            width=1.5,
            arrows=True,
            arrowsize=20,
            arrowstyle='-|>',
            connectionstyle='arc3,rad=0.1')

    # Adjust figure margins instead of using tight_layout
    plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)
    plt.axis('off')
    plt.show()
    return plt
