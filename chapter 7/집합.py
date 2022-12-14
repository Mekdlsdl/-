class Set:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)
    
    def display(self, msg):
        print(msg, self.items)
	
    def contains(self, item):
        return item in self.items

    def insert(self,elem):
        if elem in self.items:
            return
        for idx in range(len(self.items)):
            if elem < self.items[idx]:
                self.items.insert(idx, elem)
                return
        self.items.append(elem)

    def delete(self, elem):
        if elem in self.items:
            self.items.remove(elem)

    def __eq__(self, setB):
        if self.size() != setB.size():
            return False
        
        for idx in range(len(self.items)):
            if self.items[idx] != setB.items[idx]:
                return False
        
        return True

    def union(self, setB):
        newSet = Set()
        a = 0
        b = 0
        while a < len(self.items) and b < len(setB.items):
            valueA = self.items[a]
            valueB = setB.items[b]

            if valueA < valueB:
                newSet.items.append(valueA)
                a += 1

            elif valueA > valueB:
                newSet.items.append(valueB)
                b += 1

            else:
                newSet.items.append(valueA)
                a += 1
                b += 1

        while a < len(self.items):
            newSet.items.append(self.items[a])
            a += 1

        while b < len(setB.items):
            newSet.items.append(setB.items[b])
            b += 1

        return newSet


    def difference(self, setB):
        newSet = Set()
        a = 0
        b = 0

        while a < len(self.items) and b < len(setB.items):
            valueA = self.items[a]
            valueB = setB.items[b]

            if valueA < valueB:
                newSet.items.append(valueA)
                a += 1
            elif valueA > valueB:
                b += 1
            else:
                a += 1
                b += 1

        while a < len(self.items):
            newSet.items.append(self.items[a])
            a += 1

        return newSet


    def intersect(self, setB):
        newSet = Set()
        a = 0
        b = 0
        while a < len(self.items) and b < len(setB.items):
            valueA = self.items[a]
            valueB = setB.items[b]
            if valueA < valueB:
                a += 1
            elif valueA > valueB:
                b += 1
            else:
                newSet.items.append(valueA)
                a += 1
                b += 1
        
        return newSet

    
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
setA = Set()
setA.insert(1)
setA.insert(2)
setA.insert(3)
setA.insert(5)
print('setA',setA.items)

setB = Set()
setB.insert(1)
setB.insert(2)
setB.insert(3)
setB.insert(4)
print('setB',setB.items)
print()

print('union ->', setA.union(setB).items)
print('difference ->', setA.difference(setB).items)
print('intersect ->', setA.intersect(setB).items)