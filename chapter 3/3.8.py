def mergeSortList(lst1,lst2):
    ans_lst = []
    for i in range(max(len(lst1),len(lst2))):
        for j in range(len(lst1)-1):
            for k in range(len(lst2)-1):
                ans_lst.append(lst1[j])
                if lst2[k] >= lst1[j]:
                    ans_lst.insert(i,lst2[k])
    return ans_lst


lst4 = [10,20,50]
lst5 = [10,30,40]

print(mergeSortList(lst4,lst5))
