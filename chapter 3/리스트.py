class ArrayList:
    def __init__(self):
    	self.items = []

    def insert(self, pos, elem):  #O(n)->중간에 삽입할 경우 다 뒤로 밀림
        self.items.insert(pos, elem)

    def delete(self, pos): #O(n)->첫 항목을 삭제할 경우 다 앞으로 당겨야함
        return self.items.pop(pos)

    def getEntry(self, pos): return self.items[pos]
	
    def isEmpty(self): return len(self.items) == 0
	
    def size(self): return len(self.items)
	
    def clear(self): self.items = []
	
    def find(self,item): return self.items.index(item)
	
    def replace(self, pos, elem): self.items[pos] = elem
	
    def sort(self): self.items.sort()
	
    def merge(self, lst): self.items.extend(lst)
	
    def display(self, msg='ArrayList'):
        print(msg, self.size(), self.items)

        

# test --------------------------------

s = ArrayList()
s.display('단순연결리스트로 구현한 리스트(초기상태): ')
s.insert(0,10)
s.insert(0,20)
s.insert(1,30)
s.insert(s.size(),40)
s.insert(2,50)
s.display('단순연결리스트로 구현한 리스트(삽입x5): ')
s.replace(2,90)
s.display('단순연결리스트로 구현한 리스트(교체x1): ')
s.delete(2)
s.delete(s.size()-1)
s.delete(0)
s.display('단순연결리스트로 구현한 리스트(삭제x3): ')
s.clear()
s.display('단순연결리스트로 구현한 리스트(정리 후): ')
