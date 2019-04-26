#!/usr/bin/env python3
# sutimar pengpinij
# 590510137
# Lab 10
# Problem 3
# 204113 Sec 001

class Vertex:
    def __init__(self,n):
        self.name = n
        self.neighbors = list()

    def add_neighbor(self,v):
        vset = set(self.neighbors)
        # ไม่ซ้ำ
        if v not in vset:
            self.neighbors.append(v)
            self.neighbors.sort()

class Graph:
    vertices = { }
    time = 0

    def add_vertex(self,vertex):
        # มีค่าใน vertex และ ไม่มี vertex name ซ้ำ
        if isinstance(vertex,Vertex) and vertex.name not in self.vertices:
            # สร้าง dict {"ชื่อจุด(node)":เส้น} 
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


def dfs(graph, start):
    visited = [start]
    stack = [start]
    print("++++++++++++++++++++++++++++++++++++++++++")
    while stack:
        print("Stack {0}".format(stack))
        start = stack[-1]
        print("Start {0}".format(start))
        
        if start not in visited:
            visited.extend(start)
        print("Visited {0}".format(visited))

        remove_from_stack = True
        print("neighbor is {0}".format(graph.vertices[start].neighbors))
        for next in graph.vertices[start].neighbors:
            if next not in visited:
                stack.extend(next)
                remove_from_stack = False
                break

        if remove_from_stack:
            w = stack.pop()
            print("pop {0}".format(w))
        
        print("Stack {0}".format(stack))
        print("_________________________________")
    return " ".join(visited)


def main():
    g = Graph()
    dewey ="1A 11B 12C 13D 111E 131F 132G 1321H"
    node = dewey_to_node(dewey)

    # สร้างจุดว่างๆทั่ว node
    for i in node:
    	g.add_vertex(Vertex(i))

    # สร้างจุด (Obj) เชื่อมกัน
    edges = dewey_to_edges(dewey)  #['AB','AE','BF','CD','ED','DH','FG','FI','FJ','EF']
    for edge in edges:
        # แอด ตัวหน้า ตัวหลัง
        g.add_edge(edge[:1],edge[1:])
 
    d = dfs(g, node[0])
    print("dfs is {0}".format(d))
    #g.print_graph()
                           

if __name__ == '__main__':
    main()