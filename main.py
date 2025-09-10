# TARGET: Asymmetric network to solve XOR
import random
from matplotlib import pyplot as plt
import networkx as nx
import matplotlib.patches as patches

class NeuralNetwork():
    def __init__(self, number=10, input_count = 0, output_count = 0):
        self.number_of_neurons=number
        self.connections = {}
        self.network = {}
        self.input_neurons = []
        self.output_neurons = []
        self.input_nodes = input_count
        self.output_nodes = output_count
        self.debug = True
        self.inhibitors = []

    def logger(self, data):
        if self.debug:
            print(f"[DEBUG]: {data}")

    def progress(self, curr, fin):
        print(f"[{'|' * int((curr/fin)*100)}]", end="\r")

    # def buld_random_connections(self):
    #     for i in range(0)

    def build_connections(self):
        self.logger("Exploring and building connections...")
        temp = self.number_of_neurons * (self.number_of_neurons - 1) // 2
        self.logger(f"possible connections: 2^{temp}")
        runner = 2**temp
        for i in range(0, runner):
            x = random.randint(0, self.number_of_neurons-1)
            y = random.randint(0, self.number_of_neurons-1)
            if x == y:
                continue
            else:
                self.connections[i] = {
                    "neuron_i" : self.network[x],
                    "neuron_j" : self.network[y],
                    "weight" : random.random(),
                    "bias" : random.random()
                }
            self.progress(i, runner)
        self.logger("\nDone !")
        # self.logger(f"Achieved Connections: {self.connections}")

    def buildNet(self):
        for i in range(0, self.number_of_neurons):
            self.network[i] = random.random()

        while len(self.input_neurons) != self.input_nodes:
            neuron = random.randint(0, self.number_of_neurons)
            # self.logger(self.inhibitors)
            if neuron not in self.inhibitors:
                self.input_neurons.append(neuron)
                self.inhibitors.append(neuron)


        while len(self.output_neurons) != self.output_nodes:
            neuron = random.randint(0, self.number_of_neurons)
            # self.logger(self.inhibitors)
            if neuron not in self.inhibitors:
                self.output_neurons.append(neuron)
                self.inhibitors.append(neuron)

        

        self.logger(f"Total Network: {self.network}\nInitial Connections: {self.connections}")
        self.logger(f"Selected Input neurons : {self.input_neurons}")
        self.logger(f"Selected Output neurons : {self.output_neurons}")

        # self.logger(f"")

    # def pruning(self):
        # [TODO]

    #-------------------PLOTTING
    def plot_network(self):
        """Plot the neural network showing neurons and their connections"""
        fig, ax = plt.subplots(1, 1, figsize=(10, 8))
        
        # Create a graph
        G = nx.Graph()
        
        # Add nodes (neurons)
        for neuron_id in self.network.keys():
            G.add_node(neuron_id)
        
        # Add edges (connections)
        for conn_id, connection in self.connections.items():
            # Find the neuron IDs from the network
            neuron_i_id = None
            neuron_j_id = None
            
            for nid, value in self.network.items():
                if value == connection["neuron_i"]:
                    neuron_i_id = nid
                if value == connection["neuron_j"]:
                    neuron_j_id = nid
            
            if neuron_i_id is not None and neuron_j_id is not None:
                G.add_edge(neuron_i_id, neuron_j_id, weight=connection["weight"])
        
        # Generate layout
        pos = nx.spring_layout(G, seed=42)
        
        # Draw all neurons
        nx.draw_networkx_nodes(G, pos, node_color='lightblue', 
                            node_size=800, alpha=0.7)
        
        # Highlight input neurons
        if self.input_neurons:
            nx.draw_networkx_nodes(G, pos, nodelist=self.input_neurons, 
                                node_color='green', node_size=800, alpha=0.8)
        
        # Highlight output neurons
        if self.output_neurons:
            nx.draw_networkx_nodes(G, pos, nodelist=self.output_neurons, 
                                node_color='red', node_size=800, alpha=0.8)
        
        # Draw edges with weights as thickness
        edges = G.edges()
        weights = [G[u][v]['weight'] for u, v in edges]
        nx.draw_networkx_edges(G, pos, width=[w*3 for w in weights], alpha=0.6)
        
        # Draw labels
        nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
        
        # Add legend
        green_patch = patches.Patch(color='green', label='Input Neurons')
        red_patch = patches.Patch(color='red', label='Output Neurons')
        blue_patch = patches.Patch(color='lightblue', label='Hidden Neurons')
        plt.legend(handles=[green_patch, red_patch, blue_patch])
        
        plt.title("Neural Network Structure")
        plt.axis('off')
        plt.tight_layout()
        plt.show() 
    

        
        

if __name__ == "__main__":
    network = NeuralNetwork(7, 2, 1)
    network.buildNet()
    network.build_connections()
    network.plot_network()