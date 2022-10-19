items = []

def isEmpty():
    return len(items) == 0

def enqueue(item):
    items.append(item)

def dequeue():
    if not isEmpty():
        return items.pop(0)

def peek():
    if not isEmpty(): return items[-1]
