#   Generate Graph.py
# create vertices and edges

class Vertex:
    def __init__(self,n):
        self.name = n
        self.neighbors = list()

    def add_neighbor(self,v):
        vset = set(self.neighbors)
        if v not in vset:
            self.neighbors.append(v)
            self.neighbors.sort()

class Graph:
    vertices = { }
    time = 0

    def add_vertex(self,vertex):
        if isinstance(vertex,Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self,u,v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key+str(self.vertices[key].neighbors))

 
def dewey_to_edges(dewey):
	
	dewey = dewey.split(" ")
	table = {}
	for i in dewey:
	    code = i[:-1]
	    node = i[-1]
	    table[code] = node
    
   
	result = []
	for i in dewey:
		code  =i[:-2]
		node = i[-1]
		#print(code, node)
		if code != "":
			r = node + table[code]
			result.append(r)

	return result

def dewey_to_node(dewey):
	dewey = dewey.split(" ")
	result = []
	for i in dewey:
		node = i[-1]
		#print(node)
		
		result.append(node)
	return result


def main():
    g = Graph()
    # a = Vertex('A')
    # g.add_vertex(a)
    # g.add_vertex(Vertex('B'))
    # for i in range(ord('A'),ord('K')):
    #     g.add_vertex(Vertex(chr(i)))
    dewey ="1A 11B 12C 13D 111E 131F 132G 1321H"
    node = dewey_to_node(dewey)

    for i in node:
    	g.add_vertex(Vertex(i))

    edges = dewey_to_edges(dewey)  #['AB','AE','BF','CD','ED','DH','FG','FI','FJ','EF']
    for edge in edges:
        g.add_edge(edge[:1],edge[1:])
        
    g.print_graph()
                           

if __name__ == '__main__':
    main()
                  
    


