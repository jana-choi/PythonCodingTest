def bubblesort(A):
    for _ in range(1, len(A)):
        for j in range(0, len(A)-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A


if __name__ == "__main__":
    print(bubblesort([3, 2, 9, 6, 8, 1, 0, 7, 5, 4]))