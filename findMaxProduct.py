import heapq # min heap

# Finds the max product of all subarrays in [0..i]
# e.g.
# arr = [1, 2, 3, 4, 5]
# output = [-1, -1, 6, 24, 60]
def findMaxProduct(arr):
    N = len(arr)
    heap = []
    output = []
    for i, num in enumerate(arr):
        heapq.heappush(heap, num)
        if len(heap) < 3:
            output.append(-1)
            continue
        while len(heap) > 3:
            heapq.heappop(heap)  # always pops minimum
        # guaranteed to have 3 elements at all times in heap
        output.append(heap[0] * heap[1] * heap[2])
    return output

