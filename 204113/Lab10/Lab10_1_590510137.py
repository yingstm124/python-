#!/usr/bin/env python3
# sutimar pengpinij
# 590510137
# Lab 10
# Problem 1
# 204113 Sec 001

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

def dewey_edge(dewey):
    dewey = dewey.split(" ")
    
    # create A table
    table = {}
    for i in dewey:
        code = i[-1]
        node = i[:len(i)-1]
        table[node] = code
    #print(table)
   
    result = []
    for i in dewey:
        r = ""
        code = i[-1]
        node = i[:-2]
        
        if node != "":
            r = code + table[node]
            result.append(r)
    #print(result)            
    return result

def dewey_node(dewey):
	dewey = dewey.split(" ")
	ls = []
	for i in dewey:
		ls.append(i[-1])
	return ls

    
def main():
	g = Graph()
	dewey = "1A 11B 12C 13D 111E 131F 132G 1321H"
	
	node = dewey_node(dewey)
	for i in node:
		g.add_vertex(Vertex(i))

	edge = dewey_edge(dewey)
	for e in edge:
		g.add_edge(e[:1],e[1:])
	
	g.print_graph()

	
main()