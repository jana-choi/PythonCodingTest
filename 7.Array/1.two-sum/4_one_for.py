def twoSum(nums, target):
    nums_map = {}
    # 하나의 for 문으로 통합
    for i, num in enumerate(nums):
        complement = target - num
        if complement in nums_map:
            return [nums_map[complement], i]
        nums_map[num] = i

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(nums, target))