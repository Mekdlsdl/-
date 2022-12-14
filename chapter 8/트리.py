MAX_QSIZE = 10

class CircularQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [None] * MAX_QSIZE

    def isEmpty(self):
        return self.front == self.rear
    
    def isFull(self):
        return self.front == (self.rear+1) % MAX_QSIZE

    def enqueue(self,item):
        if not self.isFull():
            self.rear = (self.rear+1) % MAX_QSIZE
            self.items[self.rear] = item

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1) % MAX_QSIZE
            return self.items[self.front]
        

#---------------------------------------------------

        
class TNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def preorder(n):
    if n is not None:
        print(n.data, end = ' ')
        preorder(n.left)
        preorder(n.right)

def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data, end = ' ')
        inorder(n.right)

def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end = ' ')

def levelorder(root):
    queue = CircularQueue()
    queue.enqueue(root)
    while not queue.isEmpty():
        n = queue.dequeue()
        if n is not None:
            print(n.data, end = ' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)

def count_node(n):
    if n is None:
        return 0
    else:
        return 1 + count_node(n.left) + count_node(n.right)

def count_leaf(n):
    if n is None:
        return 0
    elif n.left is None and n.right is None:
        return 1
    else:
        return count_leaf(n.left) + count_leaf(n.right)

def calc_height(n):
    if n is None:
        return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if hLeft > hRight:
        return hLeft + 1
    else:
        return hRight + 1


# test ---------------------------------------------------

# p8.1 (1)

g = TNode('G', None, None)
h = TNode('H', None, None)
d = TNode('D', None, None)
f = TNode('F', None, None)
e = TNode('E', g, h)
c = TNode('C', e, f)
b = TNode('B', d, None)
a = TNode('A', b, c)

root = a

print('\n   In-Order : ', end = '')
inorder(root)
print('\n  Pre-Order : ', end = '')
preorder(root)
print('\n Post-Order : ', end = '')
postorder(root)
print('\nLevel-Order : ', end = '')
levelorder(root)
print()

print("노드의 개수 = %d개" %count_node(root))
print("단말의 개수 = %d개" %count_leaf(root))
print("트리의 높이 = %d개" %calc_height(root))


# p8.1 (2)

a = TNode('A', None, None)
b = TNode('B', None, None)
c = TNode('C', None, None)
d = TNode('D', None, None)
e = TNode('E', None, None)
n1 = TNode('/', a, b)
n2 = TNode('*', n1, c)
n3 = TNode('*', n2, d)
n4 = TNode('+', n3, e)

root = n4

print('\n   In-Order : ', end = '')
inorder(root)
print('\n  Pre-Order : ', end = '')
preorder(root)
print('\n Post-Order : ', end = '')
postorder(root)
print('\nLevel-Order : ', end = '')
levelorder(root)
print()

print("노드의 개수 = %d개" %count_node(root))
print("단말의 개수 = %d개" %count_leaf(root))
print("트리의 높이 = %d개" %calc_height(root))
