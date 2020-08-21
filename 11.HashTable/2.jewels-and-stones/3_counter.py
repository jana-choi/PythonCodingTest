from collections import Counter

def numJewelsInStones(J, S):
    freqs = Counter(S)
    count = 0

    for char in J:
        count += freqs[char]

    return count    


if __name__ == "__main__":
    J = "aA"
    S = "aAAbbbb"
    print(numJewelsInStones(J, S))