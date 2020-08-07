# def reverseString(s: List[str]) -> None:
def reverseString(s) -> None:
    # s.reverse()
    s[:] = s[::-1]


if __name__ == "__main__":
    s1 = ["h", "e", "l", "l", "o"]
    s2 = ["H", "a", "n", "n", "a", "h"]
    reverseString(s1)
    reverseString(s2)
    print(s1)
    print(s2)