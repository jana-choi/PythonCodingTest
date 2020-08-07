import collections

def isPalindrome(s: str) -> bool:
    # 자료형 데크로 선언
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    
    return True


if __name__ == "__main__":
    print(isPalindrome("A man, a plan, a canal: Panama"))
    print(isPalindrome("race a car"))