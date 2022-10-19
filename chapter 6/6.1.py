class Node:
    def __init__(self,elem,link=None):
        self.data = elem
        self.link = link


class LinkedStack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top == None

    def clear(self):
        self.top = None

    def push(self,item):
        n = Node(item, self.top)
        self.top = n

    def pop(self):
        if not self.isEmpty():
            n = self.top
            self.top = n.link
            return n.data

    def peek(self):
        if not self.isEmpty():
            return self.top.data

    def size(self):
        node = self.top
        count = 0
        while not node == None:
            node = node.link
            count += 1
        return count

    def display(self, msg='LinkedStack: '):
        print(msg, end = '')
        node = self.top
        while not node == None:
            print(node.data, end = ' ')
            node = node.link
        print()
        
            
    

# test --------------

string = input('단어를 입력하세요: ')
s = list(string)

stack = LinkedStack()

for i in s:
    stack.push(i)

n = int(stack.size() // 2)
count = 0

for i in range(n+1):
    if s[i] == stack.pop():
        count += 1
              
if count == (n+1) :
    print("이 문장은 회문입니다.")
else:
    print("이 문장은 회문이 아닙니다.")
