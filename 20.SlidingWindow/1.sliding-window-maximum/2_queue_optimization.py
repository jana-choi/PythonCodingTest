from collections import deque

def maxSlidingWindow(nums, k):
    results = []
    window = deque()
    current_max = float("-inf")
    
    for i, v in enumerate(nums):
        window.append(v)
        if i < k - 1:
            continue
        
        # 최대값 없는 경우 현재 요소들 중에서 최대값 설정
        if current_max == float("-inf"):
            current_max = max(window)
        # 새로 추가된 값이 기존 최대값보다 큰 경우 교체
        elif v > current_max:
            current_max = v
        
        results.append(current_max)

        # 최대값이 윈도우에서 빠지면 초기화
        if current_max == window.popleft():
            current_max = float("-inf")
    
    return results


if __name__ == "__main__":
    print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))