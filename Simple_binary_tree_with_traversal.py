from collections import deque
class TreeNode:
    def __init__(self, val) -> None:
        self.value = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, tn) -> None:
        self.root = None

    def insert(self, data):
        # Create a new node
        newNode = TreeNode(data)
        # Check if root is None -> newNode == root and return
        if self.root is None:
            self.root = newNode
            return
        # Create a queue and enqueue root 
        q = deque()
        q.append(self.root)

        # start the loop which will run indefinitely
        while True:
            # We will use the dequeue value of the queue
            cur = q.popleft()
            # If both right and left of cur is non-empty
            if cur.left is not None and cur.right is not None:
                # Add both left and right to the queue
                q.append(cur.left)
                q.append(cur.right)
            else:
                # cur.left is empty, put the new node there and return
                if cur.left is None:
                    cur.left = newNode
                    return
                # else, cur.right is empty, so put newnode here and return    
                else:
                    cur.right = newNode
                    return

    def inOrder(self):
        # left -> root -> right
        arr = []
        def rec(node):
            if node is None:
                return
            rec(node.left)
            arr.append(node.value)
            rec(node.right)
        rec(self.root)
        return arr
    def preOrder(self):
        # root -> left -> right
        arr = []
        def rec(node):
            if node is None:
                return
            arr.append(node.value)
            rec(node.left)
            rec(node.right)
        rec(self.root)
        return arr
    def postOrder(self):
        # left -> right -> root
        arr = []
        def rec(node):
            if node is None:
                return
            rec(node.left)
            rec(node.right)
            arr.append(node.value)
        rec(self.root)
        return arr

