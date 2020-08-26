from itertools import combinations

def combine(n, k):
    return list(map(list, combinations(range(1, n+1), k)))

if __name__ == "__main__":
    print(combine(4, 2))