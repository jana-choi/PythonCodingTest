import heapq

def findKthLargest(nums, k):
    heapq.heapify(nums)

    for _ in range(len(nums) - k):
        heapq.heappop(nums)
    
    return heapq.heappop(nums)


if __name__ == "__main__":
    print(findKthLargest([3,2,3,1,2,4,5,5,6], 4))