from collections import Counter
import heapq

def topKFrequent(nums, k):
    freqs = Counter(nums)
    freqs_heap = []
    # 힙에 음수로 삽입
    for f in freqs:
        heapq.heappush(freqs_heap, (-freqs[f], f))  # (value, key)
    
    topk = list()
    # k번 만큼 추출, 최소 힙(Min Heap)이므로 가장 작은 음수 순으로 추출
    for _ in range(k):
        topk.append(heapq.heappop(freqs_heap)[1])
    
    return topk


if __name__ == "__main__":
    print(topKFrequent([1, 1, 1, 2, 2, 3], 2))