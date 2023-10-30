import heapq


class Solution:
    def topKFrequent(self, nums, k):
        
        my_m = {}

        for x in nums:
            my_m[x] = my_m.get(x, 0) + 1

        largest_keys = heapq.nlargest(k, my_m, key=lambda key: my_m[key])
        return list(largest_keys)
    
    # Alternate

    #   def topKFrequent(self, nums, k):
    #         my_m = {}
        
    #     for x in nums:
    #         my_m[x] = my_m.get(x, 0) + 1
        
    #     min_heap = []

    #     for key, value in my_m.items():
    #         heapq.heappush(min_heap, (value, key))
    #         if len(min_heap) > k:
    #             heapq.heappop(min_heap)

    #     top_k_elements = [x[1] for x in min_heap]

    #     return top_k_elements