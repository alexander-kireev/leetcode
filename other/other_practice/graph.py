class Graph:
    def __init__(self):
        self.adj = {}

    def add_node(self, node):
        if node not in self.adj:
            self.adj[node] = []

    def add_edge(self, a, b):
        # undirected graph: a <-> b
        self.add_node(a)
        self.add_node(b)

        self.adj[a].append(b)
        self.adj[b].append(a)

    def neighbors(self, node):
        return self.adj.get(node, [])

    def dfs(self, start):
        if start not in self.adj:
            return []

        visited = set()
        result = []

        def visit(node):
            if node in visited:
                return

            visited.add(node)
            result.append(node)

            for neighbor in self.adj[node]:
                visit(neighbor)

        visit(start)
        return result

    def bfs(self, start):
        if start not in self.adj:
            return []

        visited = set()
        result = []
        queue = [start]

        visited.add(start)

        while queue:
            node = queue.pop(0)
            result.append(node)

            for neighbor in self.adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return result

    def connected_components(self):
        visited = set()
        components = []

        for node in self.adj:
            if node not in visited:
                component = []

                def visit(cur):
                    if cur in visited:
                        return

                    visited.add(cur)
                    component.append(cur)

                    for neighbor in self.adj[cur]:
                        visit(neighbor)

                visit(node)
                components.append(component)

        return components