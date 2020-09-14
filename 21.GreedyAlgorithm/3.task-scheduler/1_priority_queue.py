from collections import Counter

def leastInterval(tasks, n):
    counter = Counter(tasks)
    result = 0

    while True:
        sub_count = 0
        # 개수 순 추출
        for task, _ in counter.most_common(n + 1):
            sub_count += 1
            result += 1

            counter.subtract(task)
            # 0 이하인 아이템을 목록에서 완전히 제거
            counter += Counter()
        
        if not counter:
            break
    
        result += n - sub_count + 1 # n+1 만큼 나온 경우에는 idle 필요 없음. 그렇지 않은 경우에는 idle 추가
    
    return result


if __name__ == "__main__":
    print(leastInterval(["A", "A", "A", "B", "B", "B"], 2))
    print(leastInterval(["A", "A", "A", "B", "C", "D"], 2))