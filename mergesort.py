def mergesort(a):
    N = len(a)
    helper = [0] * N
    mergesortrec(a, helper, 0, N-1)

def mergesortrec(a, helper, lo, hi):
    mid = (lo + hi) // 2
    if lo < hi:
        mergesortrec(a, helper, lo, mid)
        mergesortrec(a, helper, mid+1, hi)
        merge(a, helper, lo, hi)

def merge(a, helper, lo, hi):
    mid = (lo + hi) // 2
    for i in range(lo, hi+1):
        helper[i] = a[i]

    l = lo
    r = mid+1
    curr = lo
    # Combine the 2 arrs
    while l <= mid and r <= hi:
        # print('l {} r {} curr {}'.format(l,r,curr))
        if helper[l] <= helper[r]:
            a[curr] = helper[l]
            l += 1
        else:
            a[curr] = helper[r]
            r += 1
        curr += 1
    # Copy over leftovers from left arr
    while l <= mid:
        a[curr] = helper[l]
        l += 1
        curr += 1

a = [7,6,2,4,1,3,5,8,9]
print(a)
mergesort(a)
print(a)
