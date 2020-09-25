def majorityElement(nums):
    return sorted(nums)[len(nums) // 2]


if __name__ == "__main__":
    print(majorityElement([3,2,3]))
    print(majorityElement([2,2,1,1,1,2,2]))
    print(majorityElement([1,2,1,3,1,4,1,1]))