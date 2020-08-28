from collections import defaultdict

def findItinerary(tickets):
    graph = defaultdict(list)
    # 그래프 순서대로 구성
    for a, b in sorted(tickets):
        graph[a].append(b)
    
    route, stack = [], ["JFK"]
    while stack:
        # 반복으로 스택을 구성하되 막히는 부분에서 풀어내는 처리
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop(0))
        route.append(stack.pop())
    
    # 다시 뒤집어 어휘 순 결과로
    return route[::-1]
    

if __name__ == "__main__":
    case1 = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    case2 = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    print(findItinerary(case1))
    print(findItinerary(case2))