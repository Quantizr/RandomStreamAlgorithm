def main():
    # initialize a tree with root value "psi"
    root = Tree()
    root.value = "psi"
    
    # To use as an actual stream, you would convert input binary (0s and 1s)
    # to "H"s and "T"s and pass each incoming value into:
    # RandomStream(root, value, depth)
    # where: root is the Tree defined above, value is the incoming value,
    # and depth is the maximum depth of the status tree (higher depth leads to 
    # higher entropy extraction up to theoretical bound).
    # Below we treat the string "inputFlips" as a input stream with each letter
    # being an incoming value.
    
    
    # Input coin flips, H(eads) or T(ails)
    # "HTTTHT" is the input used in Ex. 1 and Fig. 1 of the paper
    inputFlips = "HTTTHT"
    # depth is the maximum depth of the status tree
    depth = -1 # -1 is used for infinite depth
    
    
    # iterate through inputFlips as if it were a stream
    for value in inputFlips: 
        RandomStream(root, value, depth) # -1 used for infinite depth
        
        
# define a Tree class since the algorithm uses a binary status tree
class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None
        

# Implementation of Random-Stream Algorithm logic as defined in paper
# (Quoted comments are quoted from Zhou-Bruck's paper)
        
# node corresponds to "u" as described in the original paper
# y corresponds to "y" (an element of the set {H, T})
# depth corresponds to depth "d", use -1 for for infinite depth
        
# node.value corresponds to "x" (an element of the set {psi, H, T, 1, 0})
# node.left corresponds to "u_l", node.right corresponds to "u_r"
def RandomStream(node, y, depth):    
    if depth == 0: return
    
    # allow for infinite depth
    newDepth = -1
    if depth > 0: newDepth = depth - 1
    
    # "When x = φ, set x = y."
    if node.value == "psi":
        node.value = y 

    # "When x = 1 or 0, output x and set x = y."
    elif node.value == "1" or node.value == "0":        
        # Print the output stream (in this case to the console)
        print(node.value, end='', flush=True)
        
        node.value = y

    # "When x = H or T, we first check whether u has children."
    elif node.value == "H":
        if not node.left: #if node.left doesn't exist, node.right also doesn't
            # "Create two children with label φ for it."
            node.left = Tree()
            node.right = Tree()
            node.left.value = "psi"
            node.right.value = "psi"
        if y == "H": #HH
            # "Set x = φ, then pass a symbol T to u_l and a symbol H to u_r."
            node.value = "psi"
            RandomStream(node.left, "T", newDepth)
            RandomStream(node.right, "H", newDepth)
        if y == "T": #HT
            # "Set x = 1, then pass a symbol H to u_l."
            node.value = "1"
            RandomStream(node.left, "H", newDepth)

    # "When x = H or T, we first check whether u has children."
    elif node.value == "T":
        if not node.left:
            # "Create two children with label φ for it."
            node.left = Tree()
            node.right = Tree()
            node.left.value = "psi"
            node.right.value = "psi"
        if y == "T": #TT
            # "Set x = φ, then pass a symbol T to u_l and a symbol T to u_r."
            node.value = "psi"
            RandomStream(node.left, "T", newDepth)
            RandomStream(node.right, "T", newDepth)
        if y == "H": #TH
            # "Set x = 0, then pass a symbol H to u_l."
            node.value = "0"
            RandomStream(node.left, "H", newDepth)
            
        
if __name__=="__main__":
    main()