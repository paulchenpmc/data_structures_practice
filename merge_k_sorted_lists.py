# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import *

# https://leetcode.com/problems/merge-k-sorted-lists/submissions/
# Idea: maintain min heap of top of each K lists, pop lowest to build merged list
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # seed the heap
        heap = []
        counter = 0 # Counter exists only to resolve compare conflicts for same val in min heap
        for node in lists:
            if node is None:
                continue
            # Python heapq sorts tuples based on first val, then second on conflict
            heappush(heap, (node.val, counter, node))
            counter += 1
        # Iterate over lists until all are emptied
        result_head = ListNode()
        current_node = result_head
        while heap:
            min_val,_,min_node = heappop(heap)
            # print(min_val)
            if min_node.next:
                heappush(heap, (min_node.next.val, counter, min_node.next))
                counter += 1
            current_node.next = min_node
            current_node = current_node.next
        return result_head.next