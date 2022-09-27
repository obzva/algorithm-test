def quicksort(A, lo, hi):
    def partition(lo, hi):
        pivot = A[hi]
        i = lo
        for j in range(lo, hi):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                i += 1
        A[i], A[hi] = A[hi], A[i]

        return i

    if lo < hi:
        pivot = partition(lo, hi)
        quicksort(A, lo, pivot - 1)
        quicksort(A, pivot + 1, hi)
       