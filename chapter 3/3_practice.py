#3.2

lst = []

lst.insert(0,10)        #[10]
lst.insert(1,20)        #[10,20]
lst.insert(0,30)        #[30,10,20]
lst.insert(2,40)        #[30,10,40,20]
lst.insert(len(lst),50) #[30,10,40,20,50]

print(lst)



#3.3

lst.insert(1,60)        #[30,60,10,40,20,50]
lst[2]=70               #[30,60,70,40,20,50]
lst.pop(2)              #[30,60,40,20,50]

print(lst)



#3.5

def maxList(lst):
    max_lst = max(lst)
    return max_lst

print("최대 =",maxList(lst))



#3.6

def minMaxList(lst):
    max_lst = max(lst)
    min_lst = min(lst)
    ans_tup = (max_lst, min_lst)
    return ans_tup

print("(최대, 최소) =",minMaxList(lst))



#3.7

def duplicationList(lst1, lst2):
    count = 0
    for i in lst1:
        for j in lst2:
            if i == j:
                count += 1
            else:
                count += 0
    if count == 0:
        return False
    else:
        return True

lst2 = [10,20,30]
lst3 = [10,70,80,90]

print("동일한 항목 있음",duplicationList(lst,lst2))
print("동일한 항목 없음",duplicationList(lst,lst3))



#3.8
 def mergeSortList(lst1, lst2):
    i = 0
    j = 0
    k = 0
    A = []

    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            A.insert(k, lst1[i])
            i += 1
        else:
            A.insert(k, lst2[j])
            j += 1
        k += 1

    while i < len(lst1):
        A.insert(k, lst1[i])
        i += 1
        k += 1

    while j < len(lst2):
        A.insert(k, lst2[j])
        j += 1
        k += 1

    return A



lst4 = [10,20,50]
lst5 = [10,30,40]

print(mergeSortList(lst4,lst5))
           
