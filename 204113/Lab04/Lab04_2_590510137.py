#!/usr/bin/env python3
# sutimar pengpinij
# 590510137
# Lab 04
# Problem 2
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

class LinkedList(object):
    # constructure 
    def __init__(self ,r=None):
        self.root = r

    # add first
    def add(self, d):
        # next of new_node point to root 
        new_node = Node(d ,self.root)
        # change head to newnode that first of lists
        self.root = new_node

    # delete key
    def remove(self ,key):
        # setting default
        prev_node = None
        curr_node = self.root
        # finding key
        while curr_node:
            # found !!!!!
            if curr_node.get_data() == key:
                # prev_node is not None and found the key
                if prev_node:
                    # set up next between prev_node to next curr_node
                    prev_node.set_next(curr_node.get_next())
                    # remove first list
                else:
                    self.root = curr_node.get_next()
                return True
            # not found !!!
            else:
                # keep moving prev_node and curr_node
                prev_node = curr_node
                curr_node = curr_node.get_next()
        return False

    def print(self):
        # setting default
        curr_node = self.root
        # loop list of all
        while curr_node:
            print(curr_node.get_data(),end=" ")
            # moving curr_node
            curr_node = curr_node.get_next()
        # up a new line
        print("")
            
    def insert_in_order(self, d):
        # empty list
        if self.root == None:
            self.add(d)
        # checking data is minimum
        elif self.root.get_data() > d:
           # insert first node 
           self.add(d)

        # keep moving for sort min to max
        else:
            # setting default 
            curr_node = self.root
            # value of curr_node less than insert_in_order(d)
            while curr_node.get_next() and curr_node.get_next().get_data() < d:
                # moving curr_node 
                curr_node = curr_node.get_next()
            # curr_node more than data get out of loop
            new_node = Node(d, None)
            # setting new_node
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

    