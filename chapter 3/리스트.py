class ArrayList:
    def __init__(self):
    	self.items = []

    def insert(self, pos, elem):  #O(n)->중간에 삽입할 경우 다 뒤로 밀림
	items.insert(pos, elem)

    def delete(self, pos): #O(n)->첫 항목을 삭제할 경우 다 앞으로 당겨야함
	return items.pop(pos)

    def getEntry(self, pos): return items[pos]
	
    def isEmpty(self): return len(items) == 0
	
    def size(self): return len(items)
	
    def clear(self):
	items = []
	
    def find(self,item): return items.index(item)
	
    def replace(self, pos, elem): items[pos] = elem
	
    def sort(self): items.sort()
	
    def merge(self, lst): items.extend(lst)
	
    def display(self, msg='ArrayList'):
	print(msg, size(), items)
        
