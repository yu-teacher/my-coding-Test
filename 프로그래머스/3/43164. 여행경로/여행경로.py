from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    for start, end in tickets:
        graph[start].append(end)
    
    for airport in graph:
        graph[airport].sort()
    
    route = []
    def dfs(airport):
        while graph[airport]:
            next_airport = graph[airport].pop(0)
            dfs(next_airport)
        route.append(airport)
    
    dfs("ICN")
    return route[::-1]