from random import choice


class Node:
    def __init__(self, id, connections):
        self.id = id
        self.connections = connections


class Graph:
    def __init__(self, nodes=[]):
        self.nodes = nodes

    def create_node(self, id, connections):
        new_node = Node(id=id, connections=connections)
        node = []
        node.append(new_node)
        node.append(id)
        node.append(connections)
        self.nodes.append(node)

    def show_graph(self):
        print(self.nodes)

    def get_connections(self, id):
        for node in self.nodes:
            if node[0].id == id:
                return node[0].id, node[0].connections

        return None, None

    def search(self, start, end):
        explored = [start]
        path = [start]
        def explore(current_node):
            node_connections = self.get_connections(current_node)[1]
            if self.get_connections(current_node)[0] == end:
                print("end reached")
                return

            if node_connections is not None and len(node_connections) > 0:
                print(node_connections)
                path_choice = choice(node_connections)
                node_connections.remove(path_choice)
                explored.append(path_choice)
                print(path_choice)
                explore(path_choice)
            
            else:
                print("max depth reached")

                def re_explore():
                    global poped_node
                    poped_node = explored.pop()
                    try:
                        explored_node_connections = self.get_connections(poped_node)[1]
                        if explored_node_connections is not None:
                            if len(explored_node_connections) > 1:
                                explored.append(poped_node)
                            explore(poped_node)
                            return
                        re_explore()
                    except IndexError:
                        re_explore()

                re_explore()

        explore(start)


my_graph = Graph()

my_graph.create_node("dog", ["cat", "bird"])
my_graph.create_node("cat", ["mouse", "cyote", "elephent"])
my_graph.create_node("mouse", ["pig"])
my_graph.create_node("cyote", None)
my_graph.create_node("pig", ["mouse"])
my_graph.create_node("bird", None)
my_graph.create_node("elephent", ["mouse"])
my_graph.search("dog", "elephent")
