"""

692. Top K Frequent Words

Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.


Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.


Time Complexity: O(Nlogk), where N is the length of words. We count the frequency of each word in O(N) time, then we add N words
to the heap, each in O(logk) time. Finally, we pop from the heap up to k times. As k≤N, this is O(Nlogk) in total.

Space Complexity: O(N), the space used to store our count dict.

"""

def topKFrequent(words, k):
    """
    :type words: List[str]
    :type k: int
    :rtype: List[str]
    """
    import heapq
    import collections
    count = collections.Counter(words)
    heap_list = [(-fr, wr) for wr, fr in count.items() ]
    heapq.heapify(heap_list)
    return [heapq.heappop(heap_list)[1] for _ in range(k)]