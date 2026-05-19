#Step 5: Stores page relationship
import networkx as nx

class WebsiteGraph:
  
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_relationship(self, source, destination):
        self.graph.add_edge(source, destination)
        
    def get_graph(self):
        return self.graph