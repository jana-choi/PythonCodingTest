import heapq

def findKthLargest(nums, k):
    return heapq.nlargest(k, nums)[-1]


if __name__ == "__main__":
    print(findKthLargest([3,2,3,1,2,4,5,5,6], 4))