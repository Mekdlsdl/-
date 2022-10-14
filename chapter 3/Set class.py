class Set:
    def __init__(self):
        self.items = []
	
    def size(self):
        return len(self.items)
    
    def display(self, msg):
        print(msg, self.items)
	
    def contains(self, item):
        return item in self.items
    
    def insert(self, elem): #O(n2)
        if elem not in self.items:
            self.items.append(elem)

    def delete(self, elem): #O(n2)
        if elem in self.items:
            self.items.remove(elem)

    def union(self, setB): #O(n^2)
        setC = Set()
        setC.items = list(self, items)

        for elem in setB.items:
            if elem not in self.items: #n번
                setC.items.append(elem)
        return setC

    def intersect(self, setB): #O(n^2)
        setC = Set()
        for elem in setB.items:
            if elem in self.items: #n번
                setC.items.append(elem)
        return setC

    def difference(self, setB): #O(n^2)
        setC = Set()
        for elem in setB.items:
            if elem not in setB.items: #n번
                setC.items.append(elem)
        return setC


    def properSubset(self, setB):
        setC = Set()
        setD = Set()

        for elem in self.items:
            if elem in setB.items:
                setC.items.append(elem)
            else: setD.items.append(elem)

        if setC.items == setA.items and setD.size() == 0 and self.items != setB.items:
            return True
        else: return False



#test------
# 진부분집합일 경우 -> True
setA = Set()
setA.insert(1)
setA.insert(2)
setA.insert(3)
print(setA.items)

setB = Set()
setB.insert(1)
setB.insert(2)
setB.insert(3)
setB.insert(4)
print(setB.items)

print(setA.properSubset(setB))



# 진부분집합이 아닐 경우 False

setA = Set()
setA.insert(1)
setA.insert(2)
setA.insert(3)
setA.insert(5)
print(setA.items)

setB = Set()
setB.insert(1)
setB.insert(2)
setB.insert(3)
setB.insert(4)
print(setB.items)

print(setA.properSubset(setB))
