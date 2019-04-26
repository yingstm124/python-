
class Node(object):
    # constructure
    def __init__(self, d, n=None):
        self.data = d
        self.next_node = n
    # getter and setter 
    def get_next(self):
        return self.next_node
    def set_next(self , n):
        self.next_node = n
    def get_data(self):
        return self.data
    def set_data(self , d):
        self.data = d

class LinkedList(object):
    # constructure 
    def __init__(self ,r=None):
        self.root = r

    # add first
    def add(self, d):
        new_node = Node(d ,self.root)
        self.root = new_node

    # delete
    def remove(self ,key):
        # default
        prev_node = None
        curr_node = self.root
        # finding key
        while curr_node:
            # found
            if curr_node.get_data() == key:
                if prev_node:
                    prev_node.set_next(curr_node.get_next())
                else:
                    self.root = curr_node.get_next()
                return True
            else:
                prev_node = curr_node
                curr_node = curr_node.get_next()
        return False

    def print(self):
        curr_node = self.root
        # not empty list
        while curr_node:
            print(curr_node.get_data(),end=" ")
            curr_node = curr_node.get_next()
        print("")
            
    def insert_in_order(self, d):
        # check empty list
        if self.root == None:
            self.add(d)
        # checking d is minimum
        elif self.root.get_data() > d:
           # insert first node 
           self.add(d)
        # keep moving for sort min to max
        else:
            # default curr_node
            curr_node = self.root
            while curr_node.get_next() and curr_node.get_next().get_data() < d: 
                curr_node = curr_node.get_next()
            # curr_node more than data
            new_node = Node(d, None)
            new_node.set_next(curr_node.get_next())
            curr_node.set_next(new_node)

def main():

    myList = LinkedList()

    total = int(input())
    for i in range (total):
        order = input().split(" ")

        if order[0] == "i":
            myList.insert_in_order(int(order[1]))
        elif order[0] == "d":
            i = int(order[1])
            result = myList.remove(int(i))
            if result:
                print(i, "[deleted]")
            else:
                print(i, "[not deleted]")
        elif order[0] == "p":
            myList.print()


if __name__ == "__main__":
    main()

    