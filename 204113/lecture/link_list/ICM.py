class Node(object):
    def __init__(self, d, n=None ,c=0):
        self.data = d
        self.next = n

class Linkedlist(object):
    def __init__(self, r=None):
        self.root = r

    def print(self):
        curr = self.root
        while curr:
            print(curr.data,end=" ")
            curr = curr.next

    def check_prime (self, num):
        prime = True
        for i in range (2, num):
            if num%i == 0:
                return False
            else:
                prime = True
        
        return True
    
    def append(self, data):
        curr = self.root
        
        if curr == None:
            new_node = self.add(data)
            
        else:
            curr = self.root
            new_node = Node(data)
            while curr.next:
                curr = curr.next
            curr.next = new_node
        
    def add(self,d):
        new_node = Node(d)
        new_node.next = self.root
        self.root = new_node  

    # recursive prime , sort min to max
    def prime_factorize(self, x, i=2, current=None):
        if current is None:
            current = self.root

        # factor
        if x%i == 0:
            # checking prime
            check_i = self.check_prime(i)
            if check_i == True:
                # append 
                new_node = self.append(i)
            self.prime_factorize(x/i, 2,current)

        # base case 
        elif x < i:
            # add one first
            add_one = self.add(1)
            return self.root
        
        # x%i != 0 
        else:
            self.prime_factorize(x, i+1, self.root)

mylst = Linkedlist()
mylst.prime_factorize(180)
mylst.print()