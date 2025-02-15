class BinarySearchTree:
    # left: BinarySearchTree
    # right: BinarySearchTree
    # key: int
    # item: int
    # size: int
    def __init__(self, debugger = None):
        self.left = None
        self.right = None
        self.key = None
        self.item = None
        self._size = 1
        self.debugger = debugger

    @property
    def size(self):
         return self._size
       
     # a setter function
    @size.setter
    def size(self, a):
        debugger = self.debugger
        if debugger:
            debugger.inc_size_counter()
        self._size = a

    ####### Part a #######
    '''
    Calculates the size of the tree
    returns the size at a given node
    '''
    def calculate_sizes(self, debugger = None):
        # Debugging code
        # No need to modify
        # Provides counts
        if debugger is None:
            debugger = self.debugger
        if debugger:
            debugger.inc()

        # Implementation
        self.size = 1
        if self.right is not None:
            self.size += self.right.calculate_sizes(debugger)
        if self.left is not None:
            self.size += self.left.calculate_sizes(debugger)
        return self.size

    '''
    Select the ind-th key in the tree
    
    ind: a number between 0 and n-1 (the number of nodes/objects)
    returns BinarySearchTree/Node or None
    '''
    def select(self, ind):
        left_size = 0
        if self.left is not None:
            left_size = self.left.size
        if ind == left_size:
            return self
        if left_size > ind and self.left is not None:
            return self.left.select(ind)
        if left_size < ind and self.right is not None:
            return self.right.select(ind - left_size - 1)
        return None


    '''
    Searches for a given key
    returns a pointer to the object with target key or None (Roughgarden)
    '''
    def search(self, key):
        if self is None:
            return None
        elif self.key == key:
            return self
        elif self.key < key and self.right is not None:
            return self.right.search(key)
        elif self.left is not None:
            return self.left.search(key)
        return None
    

    '''
    Inserts a key into the tree
    key: the key for the new node; 
        ... this is NOT a BinarySearchTree/Node, the function creates one
    
    returns the original (top level) tree - allows for easy chaining in tests
    '''
    def insert(self, key):
        if self.key is None:
            self.key = key
        elif self.key > key: 
            if self.left is None:
                self.left = BinarySearchTree(self.debugger)
            self.left.insert(key)
        elif self.key < key:
            if self.right is None:
                self.right = BinarySearchTree(self.debugger)
            self.right.insert(key)

        # Set size to the sizes of the left and right subtrees + 1
        left_size = self.left.size if self.left is not None else 0
        right_size = self.right.size if self.right is not None else 0
        self.size = left_size + right_size + 1

        return self

    
    ####### Part b #######

    '''
    Performs a `direction`-rotate the `side`-child of (the root of) T (self)
    direction: "L" or "R" to indicate the rotation direction
    child_side: "L" or "R" which child of T to perform the rotate on
    Returns: the root of the tree/subtree
    Example:
    Original Graph
      10
       \
        11
          \
           12
    
    Execute: NodeFor10.rotate("L", "R") -> Outputs: NodeFor10
    Output Graph
      10
        \
        12
        /
       11 
    '''
    def rotate(self, direction, child_side):
        # Check if BST is None
        if self == None:
            return self
        
        # If rotation-side child is None, return self
        A = None
        if child_side == "L":
            A = self.left
        elif child_side == "R":
            A = self.right
        if A == None:
            return self
        
        a_size = A.size

        def get_size(t):
            if t == None:
                return 0
            return t.size

        if direction == "L":
            B = A.right
            if child_side == "L":
                self.left = B
                original_B_left = self.left.left
                self.left.left = A
                self.left.left.right = original_B_left
                self.left.size = a_size
                self.left.left.size = get_size(self.left.left.left) + get_size(self.left.left.right) + 1
            elif child_side == "R":
                self.right = B
                original_B_left = self.right.left
                self.right.left = A
                self.right.left.right = original_B_left
                self.right.size = a_size
                self.right.left.size = get_size(self.right.left.left) + get_size(self.right.left.right) + 1

        elif direction == "R":
            B = A.left
            if child_side == "L":
                self.left = B
                original_B_right = self.left.right
                self.left.right = A
                self.left.right.left = original_B_right
                self.left.size = a_size
                self.left.right.size = get_size(self.left.right.left) + get_size(self.left.right.right) + 1
            elif child_side == "R":
                self.right = B
                original_B_right = self.right.right
                self.right.right = A
                self.right.right.left = original_B_right
                self.right.size = a_size
                self.right.right.size = get_size(self.right.right.left) + get_size(self.right.right.right) + 1
        return self

    def print_bst(self):
        if self.left is not None:
            self.left.print_bst()
        print( self.key),
        if self.right is not None:
            self.right.print_bst()
        return self