#!/usr/bin/env python3
# sutimar pengpinij
# 590510137
# Lab 10
# Problem 2
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

def bfs(graph, start):
    output = []
    # เอา set ยัดกราฟทั้งหมด
    setV = set(graph.vertices)
    queue = []

    if start in graph.vertices :
        root = graph.vertices[start]
        setV = setV - set(root.name)
        queue.append(root)
    
    if len(queue) == 1 :
        while len(queue) > 0 :
            v = queue.pop(0)
            output.append(v.name)
            for neighbor in v.neighbors :
                if neighbor in setV :
                    # update set ลบ ตัว neighbor ออก
                    setV = setV - set(neighbor)
                    # append node ในกราฟทั้งหมด
                    queue.append(graph.vertices[neighbor])
    
    return " ".join(output)


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
 
    b = bfs(g, node[0])  
    print("bfs is {0}".format(b))
    #g.print_graph()
                           

if __name__ == '__main__':
    main()