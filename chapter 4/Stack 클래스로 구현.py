class Stack:
    def __init__(self):
        self.top = []

    def isEmpty(self):
        return len(self.top) == 0

    def push(self,item): # 대부분 O(1) / list의 전단 사용시 O(n) - 한칸씩 밀어야함
        self.top.append(item)

    def pop(self): # 항상 O(1)
        if not self.isEmpty():
            return self.top.pop(-1)

    def peek(self): # O(1)
        if not self.isEmpty():
            return self.top[-1]

    def size(self): # O(1)
        return len(self.top)

    def clear(self): # O(1)
        self.top = []



# test --------------

odd = Stack()
even = Stack()

for i in range(10):
    if i % 2 == 0: even.push(i)
    else: odd.push(i)

print('스택 even push 5회: ', even.top)
print('스택 odd  push 5회: ', odd.top)
print('스택 even     peek: ', even.peek())
print('스택 odd      peek: ', odd.peek())

for _ in range(2): even.pop()
for _ in range(3): odd.pop()
print('스택 even  pop 2회: ', even.top)
print('스택 odd   pop 3회: ', odd.top)
