import heapq
def ucs(graph, start, goal):
    queue = [(0, [start])]

    visited = set()

    while queue:
        cost, path = heapq.heappop(queue)
        node = path[-1]

        if node == goal:
            return path, cost

        if node not in visited:
            visited.add(node)

            for neighbor, weight in graph.get(node, []):
                if neighbor not in visited:
                    new_cost = cost + weight
                    new_path = path + [neighbor]
                    heapq.heappush(queue, (new_cost, new_path))
    return None, float('inf')
graph = {
    'A': [('H', 1), ('M', 4)],
    'H': [('D', 2), ('E', 5)],
    'M': [('F', 3)],
    'D': [('G', 1)],
    'E': [('G', 2)],
    'F': [('G', 1)],
    'G': []
}
start = 'A'
goal = 'G'
path, cost = ucs(graph, start, goal)
print("Path:", path)
print("Cost:", cost)