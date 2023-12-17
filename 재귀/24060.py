# 재귀 알고리즘 수업 병합정렬 1

import sys

def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    i, j, t = p, q + 1, 1
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp[t] = A[i]; t += 1; i += 1
        else:
            tmp[t] = A[j]; t += 1; j += 1
    while i <= q:
        tmp[t] = A[i]; t += 1; i += 1
    while j <= r:
        tmp[t] = A[j]; t += 1; j += 1
    i, t = p, 1
    while i <= r:
        A[i] = tmp[t]; i += 1; t += 1