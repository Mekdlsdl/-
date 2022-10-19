top = []

def isEmpty():
    return len(top) == 0

def push(item): # 대부분 O(1) / list의 전단 사용시 O(n) - 한칸씩 밀어야함
    top.append(item)

def pop(): # 항상 O(1)
    if not isEmpty():
        return top.pop(-1)

def peek(): # O(1)
    if not isEmpty():
        return top[-1]

def size(): # O(1)
    return len(top)

def clear(): # O(1)
    global top
    top = []


# test ----------

for i in range(1,6):
    push(i)
    
print('push 5회: ',top)
print('pop() -->', pop())
print('pop() -->', pop())
print('pop 2회: ',top)



push('홍길동')
push('이순신')
print('push 2회: ',top)
print('pop() -->',pop())
print('pop 1회: ',top)
