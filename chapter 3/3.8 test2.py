def mergeSortList(lst1, lst2):
    i, j, k = 0, 0, 0
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
