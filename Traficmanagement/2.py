import networkx as nx
import matplotlib.pyplot as plt

def create_graph():
    G = nx.Graph()
    G.add_edge('A', 'B', weight=4)
    G.add_edge('A', 'C', weight=8)
    G.add_edge('B', 'C', weight=2)
    return G

def calculate_shortest_path(G, source):
    return nx.shortest_path_length(G, source=source, weight='weight')       #MST feature added

def predict_traffic(G):
    # Assuming historical traffic data is a list of dictionaries
    # key : value
    historical_traffic_data = [
        {'A': 0, 'B': 5, 'C': 8},
        {'A': 0, 'B': 2, 'C': 5}
    ]

    for data in historical_traffic_data:
        for edge in G.edges():
            G[edge[0]][edge[1]]['weight'] = data[edge[1]]

        # Print shortest path for demonstration
        print(calculate_shortest_path(G, 'A'))

def main():
    G = create_graph()

    #  Degree 
    degree_centrality = nx.degree_centrality(G)
    print("Degree Centrality:", degree_centrality)

    betweenness_centrality = nx.betweenness_centrality(G)
    print("Betweenness Centrality:", betweenness_centrality)

    closeness_centrality = nx.closeness_centrality(G)
    print("Closeness Centrality:", closeness_centrality)

    # Predict traffic based on historical data
    predict_traffic(G)

    # Visualize the graph
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=20, font_weight='bold')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

if __name__ == "__main__":
    main()
