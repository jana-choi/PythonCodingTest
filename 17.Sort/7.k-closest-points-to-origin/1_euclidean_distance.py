import heapq

def kClosest(points, K):
    heap = []
    for (x, y) in points:
        dist = (x **2) + (y ** 2)
        heapq.heappush(heap, (dist, x, y))
    
    results = []
    for _ in range(K):
        (dist, x, y) = heapq.heappop(heap)
        results.append([x, y])
    return results


if __name__ == "__main__":
    print(kClosest([[1,3], [-2,2]], 1))
    print(kClosest([[3,3], [5,-1], [-2,4]], 2))