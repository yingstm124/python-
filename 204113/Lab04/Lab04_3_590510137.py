#!/usr/bin/env python3
# sutimar pengpinij
# 590510137
# Lab 04
# Problem 3
# 204113 Sec 001


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

class LinkedList:
    def __init__(self, r=None):
        self.root = r

    # add-last
    def append(self, d):
        # setting default
        curr_node = self.root
        # empty list
        if self.root == None:
            return self.add(d)

        while curr_node.get_next():
            # moving next of curr_node
            curr_node = curr_node.get_next()
        # setting curr_node
        curr_node.set_next(Node(d))
        
    # recursive reverse print
    def rprint(self,curr=None):
        current = curr
        # setting current = head
        if current == None:
            current = self.root
        # last node 
        if current.get_next() == None:
            print(current.get_data(),end=" ")
            return
        self.rprint(current.get_next())
        # when finish recursive print taill to head
        print(current.get_data(),end=" ")
        
    
    def add(self, d):
        new_node = Node(d ,self.root)
        self.root = new_node

    # delete
    def remove(self ,key):
        prev_node = None
        curr_node = self.root
        while curr_node:
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
        while curr_node:
            print(curr_node.get_data(),end=" ")
            curr_node = curr_node.get_next()
        print("")
            
    def insert_in_order(self, d):
        if self.root == None:
            self.add(d)
        elif self.root.get_data() > d: 
           self.add(d)
        else:
            curr_node = self.root
            while curr_node.get_next() and curr_node.get_next().get_data() < d: 
                curr_node = curr_node.get_next()
            new_node = Node(d, None)
            new_node.set_next(curr_node.get_next())
            curr_node.set_next(new_node)

def main():
    data_ls = input().split(" ")
    lst = LinkedList()
    # print lst fist line 
    for i in data_ls:
        i = int(i)
        print(i,end=" ")
    print("")
    
    # reverse print second line
    for i in data_ls:
        lst.append(i)
    lst.rprint()
     

if __name__ == "__main__":
    main()