#   Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Example 1:

# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# Example 2:

# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
  
  
  
  
  
  def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[0:k]
        heapq.heapify(heap)
        
        for ele in nums[k:]:
            if ele > heap[0]:
                heapq.heappushpop(heap, ele)
        return heap[0]

# min heap