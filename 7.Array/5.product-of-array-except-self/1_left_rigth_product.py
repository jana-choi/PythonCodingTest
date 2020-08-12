def productExceptSelf(nums):
    out = []
    
    # 왼쪽 곱셈
    p = 1
    for i in range(len(nums)):
        out.append(p)
        p = p * nums[i]
    
    # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
    p = 1
    for i in range(len(nums)-1, -1, -1):
        out[i] = out[i] * p
        p = p * nums[i]
    
    return out

if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    print(productExceptSelf(nums))