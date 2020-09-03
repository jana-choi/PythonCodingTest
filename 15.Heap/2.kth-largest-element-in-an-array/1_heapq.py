import heapq

def findKthLargest(nums, k):
    heap = list()
    for n in nums:
        heapq.heappush(heap, -n)
    
    for _ in range(k-1):
        heapq.heappop(heap)
    
    return -heapq.heappop(heap)


if __name__ == "__main__":
    print(findKthLargest([3,2,3,1,2,4,5,5,6], 4))