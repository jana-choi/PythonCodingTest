from collections import defaultdict

def numJewelsInStones(J, S):
    freqs = defaultdict(int)
    count = 0

    for char in S:
        freqs[char] += 1

    for char in J:
        count += freqs[char]

    return count    


if __name__ == "__main__":
    J = "aA"
    S = "aAAbbbb"
    print(numJewelsInStones(J, S))