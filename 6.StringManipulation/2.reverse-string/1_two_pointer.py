# def reverseString(s: List[str]) -> None:
def reverseString(s) -> None:
    left, right = 0, len(s)-1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


if __name__ == "__main__":
    s1 = ["h", "e", "l", "l", "o"]
    s2 = ["H", "a", "n", "n", "a", "h"]
    reverseString(s1)
    reverseString(s2)
    print(s1)
    print(s2)