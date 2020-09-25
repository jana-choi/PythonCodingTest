def majorityElement(nums):
    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]
    
    half = len(nums) // 2
    a = majorityElement(nums[:half])
    b = majorityElement(nums[half:])

    return [b, a][nums.count(a) > half]


if __name__ == "__main__":
    print(majorityElement([3,2,3]))
    print(majorityElement([2,2,1,1,1,2,2]))
    print(majorityElement([1,2,1,3,1,4,1,5]))