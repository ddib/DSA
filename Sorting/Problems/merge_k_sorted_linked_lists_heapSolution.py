"""
For your reference:
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
"""
import heapq
def merge_k_lists(lists):
    """
    Problem:
    Given k linked lists where each one is sorted in the ascending order, 
    merge all of them into a single sorted linked list.
    https://leetcode.com/problems/merge-k-sorted-lists

    Complexity:
    * Time: O(nlog(k))
    * Space: O(k) 
    """
    
    n = len(lists)
    if n == 0:
        return None
    if n == 1:
        return lists[0]
        
    head = LinkedListNode(0)
    tail = head
    aux = []

    # build heap
    for i in range(n):
        if lists[i]:
            aux.append((lists[i].value, i))          
    heapq.heapify(aux)

    # get min and update heap
    while aux:
        min_value, i = heapq.heappop(aux)
        tail.next = lists[i]
        tail = tail.next
        
        if lists[i].next:
            lists[i] = lists[i].next
            heapq.heappush(aux, (lists[i].value, i))
        
        tail.next = None   
        
    return head.next 
