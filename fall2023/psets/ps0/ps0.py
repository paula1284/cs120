#################
#               #
# Problem Set 0 #
#               #
#################


#
# Setup
#
class BinaryTree:
    def __init__(self, root):
        self.root: BTvertex = root
 
class BTvertex:
    def __init__(self, key):
        self.parent: BTvertex = None
        self.left: BTvertex = None
        self.right: BTvertex = None
        self.key: int = key
        self.size: int = None

#
# Problem 1a
#

# Input: BTvertex v, the root of a BinaryTree of size n
# Output: Up to you
# Side effect: sets the size of each vertex n in the
# ... tree rooted at vertex v to the size of that subtree
# Runtime: O(n)
def calculate_sizes(v):
    if v == None:
        return 0
    else:
        v.size = 1 + calculate_sizes(v.left) + calculate_sizes(v.right)
    return v.size

#
# Problem 1c
#

# Input: BTvertex r, the root of a size-augmented BinaryTree T
# ... of size n and height h
# Output: A BTvertex that, if removed from the tree, would result
# ... in disjoint trees that all have at most n/2 vertices
# Runtime: O(h)
def find_vertex(r): 
    # Helper function to check if the tree rooted at vertex "child" has size 
    # less than r.size / 2
    def check_child(child):
        if child == None or child.size <= r.size / 2:
            return True
        return False
            
    # Return a descendent vertex if their size is greater than r.size / 2
    if not check_child(r.left):
        return find_vertex(r.left)
    elif not check_child(r.right):
        return find_vertex(r.right)
    
    # Return parent vertex if neither child has size > r.size / 2
    return r
