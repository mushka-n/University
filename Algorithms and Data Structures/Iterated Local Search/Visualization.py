import matplotlib.pyplot as plt
import networkx as nx


def Visualize_Graph(dots, path):
    dots_num = len(dots)
    G = nx.Graph()
    for dot in dots:
        G.add_node(dot.id, pos=(dot.x, dot.y))
    for i in range(dots_num - 1):
        G.add_edge(path[i], path[i + 1])
    nx.draw(G, nx.get_node_attributes(G, 'pos'), with_labels=True, )
    plt.savefig("graph_path.png")
    plt.show()
