class Node(object):
    def __init__(self ,d):
        self.data = d
        self.leftchild = None
        self.rightchild = None


class BST(object):
    def __init__(self):
        self.root = None
        
    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(self.root, value)
            
    def _add(self, moving_root, value):
        # ไปซ้าย 
        if moving_root.data > value:
            # แอดได้เลย
            if moving_root.leftchild is None:
                moving_root.leftchild = Node(value)
            # แอดไม่ได้ต้องวิ่งไปถามลูกมันอีกที
            else:
                self._add(moving_root.leftchild ,value)
        # ไปขวา
        else:
            if moving_root.rightchild is None:
                moving_root.rightchild = Node(value)
            else:
                self._add(moving_root.rightchild, value)

    def printTree(self):

        if self.root is None:
            print("None")
        else:
            self._printTree(self.root)
            
    def _printTree(self, moving_root):
        
        if moving_root is not None:
            self._printTree(moving_root.leftchild)
            print(moving_root.data, end=" ")
            self._printTree(moving_root.rightchild)
        
tree = BST()
tree.add(5)
tree.add(3)
tree.add(7)
tree.add(4)
tree.add(8)
tree.add(1)
tree.add(6)
tree.printTree()
        
