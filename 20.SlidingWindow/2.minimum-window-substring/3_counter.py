from collections import Counter

def minWindow(s, t):
    t_count = Counter(t)
    current_count = Counter()

    start = float("-inf")
    end = float("inf")

    left = 0
    # 오른쪽 포인터 이동
    for right, char in enumerate(s, 1):
        current_count[char] += 1

        # AND 연산 결과로 왼쪽 포인터 이동 판단
        while current_count & t_count == t_count:
            if right - left < end - start:
                start, end = left, right
            
            current_count[s[left]] -= 1
            left += 1
    
    return s[start:end] if end - start <= len(s) else ""


if __name__ == "__main__":
    print(minWindow("ADOBECODEBANC", "ABC"))