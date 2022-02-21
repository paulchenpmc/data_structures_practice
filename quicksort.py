def quicksort(a, l, r):
    index = partition(a, l, r)
    # Sort left half
    if l < index-1:
        quicksort(a,l,index-1)
    # Sort right half
    if index < r:
        quicksort(a,index,r)

def partition(a, l, r):
    pivot = a[(l+r) // 2]

    while l <= r:
        # Search for unsorted val
        while a[l] < pivot:
            l+=1
        # Search for unsorted val
        while a[r] > pivot:
            r-=1
        # Swap
        if l <= r:
            tmp = a[l]
            a[l] = a[r]
            a[r] = tmp
            l+=1
            r-=1
    return l


a = [7,6,2,4,1,3,5,8,9]
print(a)
quicksort(a, 0, len(a)-1)
print(a)