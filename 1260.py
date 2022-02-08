def graph(edges):
    graph_dic = dict()
    for i in range(1, N+1):
        graph_dic.setdefault(i, [])
    for s, d in edges:
        graph_dic[s].append(d)
        graph_dic[d].append(s)
    return graph_dic

def dfs(node, graph, visited=[]):
    visited.append(node)
    for i in sorted(graph[node]):
        if i not in visited:
            dfs(i, graph, visited)
    return visited

def bfs(node, graph):
    from collections import deque
    queue = deque([node])
    visited = [node]

    while queue:
        v = queue.popleft()
        for i in sorted(graph[v]):
            if i not in visited:
                queue.append(i)
                visited.append(i)
    return visited

if __name__ == '__main__':
    import sys

    N, M, V = map(int, sys.stdin.readline().rstrip().split())
    edges = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(M)] #[(1,2),(2,3),...)]
    g = graph(edges)
    print(*dfs(V, g)) #[1,2,3,4] => 1,2,3,4
    print(*bfs(V, g))