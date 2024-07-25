class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            
            if left < n and arr[left] > arr[largest]:
                largest = left
            
            if right < n and arr[right] > arr[largest]:
                largest = right
            
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)
        
        def heap_sort(arr):
            n = len(arr)
            
            # Build a maxheap
            for i in range(n // 2 - 1, -1, -1):
                heapify(arr, n, i)
            
            # One by one extract elements
            for i in range(n - 1, 0, -1):
                arr[i], arr[0] = arr[0], arr[i]  # Swap
                heapify(arr, i, 0)
        
        heap_sort(nums)
        return nums
