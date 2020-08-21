def numJewelsInStones(J, S):
    freqs = dict()
    count = 0

    for char in S:
        if char not in freqs:
            freqs[char] = 1
        else:
            freqs[char] += 1
    
    for char in J:
        if char in freqs:
            count += freqs[char]
    
    return count


if __name__ == "__main__":
    J = "aA"
    S = "aAAbbbb"
    print(numJewelsInStones(J, S))