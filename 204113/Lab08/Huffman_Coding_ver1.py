class Node(object):
    def __init__(self, d, l=None, r=None):
        self.data = d
        self.leftnode = l
        self.rightnode = r

def huffman(freq):

    # base case
    if len(freq) == 2:
        return dict(zip(freq.keys(), ["0","1"]))

    k_lowest, k_low = find_lower_(freq)
    val_lowest, val_low = freq.pop(k_lowest), freq.pop(k_low)
    freq[k_lowest + k_low] = val_lowest + val_low

    print(freq)
    print(k_lowest, k_low)
    root = huffman(freq)
    pos = root.pop(k_lowest + k_low)
    root[k_lowest], root[k_low] = pos + "0", pos + "1"
    print(root)
    print(k_lowest, k_low)

    return root

def find_lower_(freg):
    # kv[1] = value
    key_sort_freg = sorted(freg.items(), key=lambda kv:kv[1])
    return key_sort_freg[0][0], key_sort_freg[1][0]

def main():
    ex1 = {'a': 35, 'b': 26, 'c': 12,'d': 16, 'e': 17, 'f': 20}
    print(huffman(ex1))


if __name__ == "__main__":
    main()