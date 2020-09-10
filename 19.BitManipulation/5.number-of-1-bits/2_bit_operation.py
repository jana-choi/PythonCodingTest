def hammingWeight(n):
    count = 0
    while n:
        # 1을 뺀 값과 AND 연산 횟수 측정
        n &= n - 1
        count += 1
    return count

if __name__ == "__main__":
    print(hammingWeight(0b00000000000000000000000000001011))
    print(hammingWeight(0b00000000000000000000000010000000))
    print(hammingWeight(0b11111111111111111111111111111101))