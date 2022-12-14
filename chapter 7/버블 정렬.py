def printStep(arr, val):
    print(" Step %2d = "%val, end='')
    print(arr)

def bubble_sort(A):
    n = len(A)
    for i in range(n-1, 0, -1):
        bChanged = False
        for j in range(i):
            if A[j]>A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                bChanged = True

        if not bChanged:
            break
        
        printStep(A, n-i)


# ---------------------------------------
data = [5,3,8,4,9,1,6,2,7]
print("Original :", data)
bubble_sort(data)
print("Selection :", data)