def findKthLargest(nums, k):
    # nums.sort()
    # return nums[-k]
    return sorted(nums, reverse=True)[k-1]


if __name__ == "__main__":
    print(findKthLargest([3,2,3,1,2,4,5,5,6], 4))