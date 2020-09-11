from collections import Counter

def characterReplacement(s, k):
    left = right = 0
    counts = Counter()
    for right in range(1, len(s)+1):
        counts[s[right-1]] += 1
        
        # 가장 흔하게 등장하는 문자 탐색
        max_char_n = counts.most_common(1)[0][1]

        # k 초과시 왼쪽 포인터 이동
        if right - left - max_char_n > k:
            counts[s[left]] -= 1
            left += 1
    
    return right - left


if __name__ == "__main__":
    print(characterReplacement("AAABBC", 3))
    print(characterReplacement("AAABBC", 2))
    print(characterReplacement("AAABBC", 1))