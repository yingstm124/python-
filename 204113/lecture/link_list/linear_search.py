class Node(object):
    def __init__(self, d, n=None):
        self.data = d
        self.next = n


class Linkedlist(object):
    def __init__(self, r=None):
        self.root = r
    
    def make_node_list(self, data):
        new_node = Node(data)
        new_node.next = self.root
        self.root = new_node

    def linear_search(self, key, data_ls):
        mylst = Linkedlist()
        for i in range (len(data_ls)-1,-1,-1):
            mylst.make_node_list(data_ls[i])
        # search
        index = 0
        curr = mylst.root
        while curr:
            if curr.data == key:
                found = True
                break
            else:
                index += 1
                found = False
            curr = curr.next
        
        if found:
            return index
        else:
            return None


def main():
    mode = int(input())

    assert (linear_search(3, [1, 2, 3, 4, 5]) == 2)
    assert (linear_search('D', ['A', 'B', 'C', 'D', 'E']) == 3)
    assert (linear_search(3.1, [1.0, 2.1, 3.0, 3.1, 4]) == 3)
    assert (linear_search("dog", ["dog","cat","rat"]) == 0)
    assert (linear_search(3, [1, 2, 8, 4, 3]) == 4)
    assert (linear_search("D", ["A", "D", "C", "E"]) == 1)
    assert (linear_search(3.1, [1.0, 2.1, 3.0, 4, 3.1]) == 4)
    assert (linear_search(56, [1, 56, 3.0, 3.1, 4]) == 1)
    assert (linear_search("Ying", ["Breeze","Two","Ying","Wish"]) == 2)
    assert (linear_search(5, [1, 56, 3.0, 8, 4, 5]) == 5)
            
if __name__ == "__main__":
    main()