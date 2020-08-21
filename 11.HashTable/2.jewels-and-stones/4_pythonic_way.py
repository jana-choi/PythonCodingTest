
def numJewelsInStones(J, S):
    return sum(s in J for s in S)


if __name__ == "__main__":
    J = "aA"
    S = "aAAbbbb"
    print(numJewelsInStones(J, S))