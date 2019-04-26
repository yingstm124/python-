class Node(object):
    def __init__(self, d, n=None ,c=0):
        self.data = d
        self.next = n
        self.count = c

class Linkedlist(object):
    def __init__(self, r=None):
        self.root = r
    
    def create_node(self):
        word_ls = ["a","e","i","o","u"]
        for i in range (len(word_ls)-1,-1,-1):
            new_node = Node(word_ls[i])
            new_node.next = self.root
            self.root = new_node


    def vowelCount(self, word):
        word_ = Linkedlist()
        word_.create_node()
        
        for str_ in word:
            curr = word_.root
            while curr:
                if curr.data == str_:
                    curr.count += 1
                curr = curr.next 

        # print
        count = 0
        curr = word_.root
        while curr:
            count = count + curr.count
            curr = curr.next
        print(count)

def main():
    mylst = Linkedlist()
    mylst.vowelCount("puzzle games")

if __name__ == "__main__":
    main()