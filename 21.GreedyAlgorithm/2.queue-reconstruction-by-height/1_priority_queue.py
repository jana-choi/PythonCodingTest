import heapq

def reconstructQueue(people):
    heap = []
    # 키 역순, 인덱스 삽입
    for person in people:
        heapq.heappush(heap, (-person[0], person[1]))
    
    result = []
    # 키 역순, 인덱스 추출
    while heap:
        person = heapq.heappop(heap)
        result.insert(person[1], [-person[0], person[1]])
    
    return result


if __name__ == "__main__":
    print(reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))