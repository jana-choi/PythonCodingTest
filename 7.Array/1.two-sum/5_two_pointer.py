def twoSum(nums, target):
    left, right = 0, len(nums)-1
    while not left == right:
        cur_sum = nums[left] + nums[right]
        # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
        if cur_sum > target:
            right -= 1
        # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
        elif cur_sum < target:
            left += 1
        else:
            return [left, right]

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(nums, target))