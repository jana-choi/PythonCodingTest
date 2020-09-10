def getSum(a, b):
    MASK = 0xFFFFFFFF
    INT_MAX = 0x7FFFFFFF

    # 합, 자릿수 처리
    while b != 0:
        a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
    
    if a > INT_MAX:
        a = ~(a ^ MASK)
    
    return a

if __name__ == "__main__":
    print(getSum(1, 2))
    print(getSum(-2, 3))
    print(getSum(-1, -2))