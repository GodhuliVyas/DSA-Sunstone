import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.community import girvan_newman

# Create a graph
G = nx.Graph()

# Add nodes (users)
G.add_nodes_from([1, 2, 3, 4, 5])

# Add edges (relationships/interactions)
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)])

# Display the graph information
print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())
print("Nodes:", list(G.nodes()))
print("Edges:", list(G.edges()))

degree_centrality = nx.degree_centrality(G)
print("Degree Centrality:", degree_centrality) #measures the number of direct connections (edges) a node has.

# centrality of  node 1 = 2 , connected to 2, 3 
# centrality of  node 2 and 3  = 2 , connected to 4, 1 
# centrality of  node 4 = 3 , connected to 3,2,5

betweenness_centrality = nx.betweenness_centrality(G)
print("Betweenness Centrality:", betweenness_centrality) # Counts how often a node appears on shortest paths between other nodes.

# 4 lies through 3 pairs, namely 3, 2 and 5 and is the shortest


closeness_centrality = nx.closeness_centrality(G)
print("Closeness Centrality:", closeness_centrality) #measures how close a node is to all other nodes in the network.
# 4 is closest to node 5 , 3, 2 , except for node 1. 

communities = girvan_newman(G)
first_community = next(communities)
print("Communities:", first_community)

pos = nx.spring_layout(G)

# Add visuals
plt.figure(figsize=(10, 7))
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=10)

# Highlight key users based on degree centrality
node_color = ['red' if degree_centrality[node] > 0.5 else 'lightblue' for node in G.nodes()]
nx.draw_networkx_nodes(G, pos, node_color=node_color, node_size=500)

# Highlight communities
colors = ['yellow', 'green', 'blue', 'orange', 'purple']
for i, community in enumerate(first_community):
    nx.draw_networkx_nodes(G, pos, nodelist=list(community), node_color=colors[i], node_size=500, alpha=0.8)

plt.title("Social Network Analysis")
plt.show()
