def sortColors(nums):
    red, white, blue = 0, 0, len(nums)
    mid = 1

    while white < blue:
        if nums[white] < mid:
            nums[red], nums[white] = nums[white], nums[red]
            white += 1
            red += 1
        elif nums[white] > mid:
            blue -= 1
            nums[blue], nums[white] = nums[white], nums[blue]
        else:
            white += 1


if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]
    sortColors(nums)
    print(nums)