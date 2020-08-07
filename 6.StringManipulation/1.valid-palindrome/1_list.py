def isPalindrome(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    
    # 팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    
    return True


if __name__ == "__main__":
    # s = input()
    # print(isPalindrome(s))
    print(isPalindrome("A man, a plan, a canal: Panama"))
    print(isPalindrome("race a car"))