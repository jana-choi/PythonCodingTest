def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid
    
    return -1
    

if __name__ == "__main__":
    print(search([-1, 0, 3, 5, 9, 12], 9))