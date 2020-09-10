def hammingWeight(n):
    return bin(n).count("1")

if __name__ == "__main__":
    print(hammingWeight(0b00000000000000000000000000001011))
    print(hammingWeight(0b00000000000000000000000010000000))
    print(hammingWeight(0b11111111111111111111111111111101))