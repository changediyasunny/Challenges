"""

Given a max heap as an array, return the top k elements. Do not modify heap or copy entire heap to a different data structure. Example:
    15
  /    \
13      12
/  \    /
10  8	9

int[] arr = {15,13,12,10,8,9};
List<Integer> peekTopK(int[] arr, int k)
Expected output for k = 5 ==> [15,13,12,10,9]

"""

def priority_queue(temp_list):
    # Max heap largest element
    heapq.heapify(temp_list)
    n = temp_list[-1]
    temp_list = temp_list[:-1]
    return n, temp_list

def top_k_heap(heap_array, k):
    result = []
    if k > 0:
        result.append(heap_array[0])
        k -= 1
    kids = []
    i = 0
    while k:
        left = 2*i+1
        right = left + 1
        if left < len(heap_array):
            kids.append(heap_array[left])
        if right < len(heap_array):
            kids.append(heap_array[right])

        if k > 0:
            """ priority queue """
            # n, kids = priority_queue(kids)
            # result.append(n)
            """ Sorting """
            kids.sort()
            result.append(kids.pop())
        k -= 1
        i += 1
    return result

print(top_k_heap(heap_array, k))
