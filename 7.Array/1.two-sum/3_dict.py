def twoSum(nums, target):
    nums_map = {}
    # 키와 값을 바꿔서 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num] = i
    
    # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        complement = target - num
        if complement in nums_map and i != nums_map[complement]:
            # return [nums.index(num), nums_map[complement]]
            return [i, nums_map[complement]]

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(nums, target))