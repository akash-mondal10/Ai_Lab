from collections import deque
def bfs(graph, s, t):
    q, vis, par = deque([s]), {s}, {s: None}
    explored = 0
    while q:
        u = q.popleft(); explored += 1
        if u == t: break
        for v in graph[u]:
            if v not in vis:
                vis.add(v); par[v] = u; q.append(v)
    return build_path(par, s, t), explored
def dfs(graph, s, t):
    st, vis, par = [s], {s}, {s: None}
    explored = 0
    while st:
        u = st.pop(); explored += 1
        if u == t: break
        for v in graph[u]:
            if v not in vis:
                vis.add(v); par[v] = u; st.append(v)
    return build_path(par, s, t), explored

def bi_bfs(graph, s, t):
    if s == t: return [s], 1
    qs, qt = deque([s]), deque([t])
    vs, vt = {s}, {t}
    ps, pt = {s: None}, {t: None}
    explored = 0

    while qs and qt:
        # from start
        for _ in range(len(qs)):
            u = qs.popleft(); explored += 1
            for v in graph[u]:
                if v not in vs:
                    vs.add(v); ps[v] = u; qs.append(v)
                    if v in vt:
                        return join_paths(ps, pt, v), explored
        # from target
        for _ in range(len(qt)):
            u = qt.popleft(); explored += 1
            for v in graph[u]:
                if v not in vt:
                    vt.add(v); pt[v] = u; qt.append(v)
                    if v in vs:
                        return join_paths(ps, pt, v), explored
    return None, explored
def build_path(par, s, t):
    if t not in par: return None
    path = []
    cur = t
    while cur is not None:
        path.append(cur)
        cur = par[cur]
    return path[::-1]

def join_paths(ps, pt, meet):
    left = []
    x = meet
    while x is not None:
        left.append(x); x = ps[x]
    left = left[::-1]
    right = []
    x = pt[meet]
    while x is not None:
        right.append(x); x = pt[x]
    return left + right
if __name__ == "__main__":
    city = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F", "G"],
        "F": ["C", "E", "H"],
        "G": ["E", "H"],
        "H": ["F", "G"]
    }
    s, t = "A", "H"
    p1, n1 = bfs(city, s, t)
    p2, n2 = dfs(city, s, t)
    p3, n3 = bi_bfs(city, s, t)
    print("BFS path:", p1, "| nodes:", n1)
    print("DFS path:", p2, "| nodes:", n2)
    print("Bi-BFS path:", p3, "| nodes:", n3)

