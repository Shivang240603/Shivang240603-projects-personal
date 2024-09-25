import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.animation import FuncAnimation

# Function to generate a neural network-like graph
def generate_neural_network(num_neurons, num_connections):
    G = nx.DiGraph()  # Directed graph to simulate neuron flow
    for i in range(num_neurons):
        G.add_node(i)
        
    for _ in range(num_connections):
        src = np.random.randint(0, num_neurons)
        dest = np.random.randint(0, num_neurons)
        G.add_edge(src, dest)
    
    return G

# Initialize the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# Generate a neural network with 30 neurons and 60 connections
G = generate_neural_network(30, 60)

# Layout for the neural network
pos = nx.spring_layout(G)

# Draw the initial network
def draw_neural_network():
    ax.clear()
    nx.draw_networkx_nodes(G, pos, ax=ax, node_size=300, node_color="skyblue")
    nx.draw_networkx_edges(G, pos, ax=ax, edge_color="gray")
    nx.draw_networkx_labels(G, pos, ax=ax, font_size=10)
    ax.set_title("Neurons Flowing", fontsize=20)

# Animation function to update the flow of connections
def update(frame):
    ax.clear()
    
    # Add a random new connection to simulate neuron flow
    src = np.random.randint(0, len(G.nodes))
    dest = np.random.randint(0, len(G.nodes))
    G.add_edge(src, dest)
    
    # Redraw the neural network
    nx.draw_networkx_nodes(G, pos, ax=ax, node_size=300, node_color="skyblue")
    nx.draw_networkx_edges(G, pos, ax=ax, edge_color="gray", width=2)
    nx.draw_networkx_labels(G, pos, ax=ax, font_size=10)
    
    ax.set_title("Neurons Flowing", fontsize=20)

# Create the animation
ani = FuncAnimation(fig, update, frames=100, interval=500)

# Show the animation
plt.show()
