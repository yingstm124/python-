#!/usr/bin/python

class Node:

    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val


class BST:

    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self.add_(self.root, val)
    
    def add_(self, move, val):
        if val < move.v:
            if move.l is None:
                move.l = Node(val)
            else:
                self.add_(move.l, val)
        else:
            if move.r is None:
                move.r = Node(val)
            else:
                self.add_(move.r, val)

    def find(self, val): 
        if self.root is None:
            found = False
        else:
            found = self.find_(self.root, val)
        
        return found
        
    def find_(self, move, val):
        if move is None:
            found = False
        elif val < move.v:
            found = self.find_(move.l, val)
        elif val > move.v:
            found = self.find_(move.r, val)
        elif val == move.v:
            found = True
        
        return found

        
    def printTree(self):
        if(self.root is not None):
            self._printTree(self.root)
        print()

    def _printTree(self, node):
        if(node is not None):
            self._printTree(node.l)
            print(str(node.v),end=" ")
            self._printTree(node.r)


def main():

    tree = BST()
    tree.add(4)
    tree.add(6)
    tree.add(2)
    tree.add(20)
    tree.add(1)
    tree.add(3)
    tree.add(18)
    tree.printTree()
    print(tree.find(3))
    print(tree.find(32))

if __name__ == '__main__':
    main()