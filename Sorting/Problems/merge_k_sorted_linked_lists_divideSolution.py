"""
For your reference:
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
"""
def merge_k_lists(lists):
    """
    Problem:
    Given k linked lists where each one is sorted in the ascending order, 
    merge all of them into a single sorted linked list.
    https://leetcode.com/problems/merge-k-sorted-lists

    Complexity:
    * Time: O(nlog(k))
    * Space: O(1) 
    """
    
    def merge_2_lists(list1, list2):
        head = LinkedListNode(0)
        tail = head
        while list1 and list2:
            if list1.value <= list2.value:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
            tail.next = None
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        return head.next
        
    k = len(lists)
    if k == 0:
        return None
    
    last = k - 1
    while last > 0:
        i = 0
        j = last
        while j > i:
            lists[i] = merge_2_lists(lists[i], lists[j])
            i += 1
            j -= 1
        last = j
    return lists[0]
