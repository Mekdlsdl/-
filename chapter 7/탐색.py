# 순차 탐색
def sequential_search(A, key, low, high):
    for i in range(low, high+1):
        if A[i] == key:
            return i
    return None


# 이진 탐색
def binary_search(A, key, low, high):
    if low <= high:
        middle = (low + high) // 2

        if key == A[middle]:
            return middle
        elif key < A[middle]:
            return binary_search(A, key, low, middle-1)
        else:
            return binary_search(A, key, middle+1, high)
    return None

# 이진 탐색 (반복 구조)
def binary_search_iter(A, key, low, high):
    while low <= high:
        middle = (low + high) // 2
        if key == A[middle] :
            return middle
        elif key > A[middle] :
            low = middle + 1
        else:
            high = middle - 1
    return None


# 보간 탐색
def interpolation_search(A, key, low, high):
    if low <= high:
        middle = int(low + (high - low) * (key - A[low] ) / (A[high]  - A[low]))

        if key == A[middle] :
            return middle
        elif key < A[middle] :
            return binary_search(A, key, low, middle-1)
        else:
            return binary_search(A, key, middle+1, high)
    return None


# test ----------------------------

A = {0:9,1:5,2:8,3:3,4:7}
key = 8
print(f"순차 탐색 : {key} -> {sequential_search(A, key, 0, 4)}번 인덱스")
print(f"이진 탐색 : {key} -> {binary_search(A, key, 0, 4)}번 인덱스")
print(f"보간 탐색 : {key} -> {interpolation_search(A, key, 0, 4)}번 인덱스")