from queue import LifoQueue, PriorityQueue, Queue
from typing import *

V = TypeVar("V")
E = TypeVar("E")


class Graph(object):
    def __init__(self, g={}, directed=False):
        super().__init__()
        self._g = g
        self._info = {"Directed": directed}

    def add_vertx(self, x: V):
        if x in self._g:
            return
        self._g[x] = set()

    def add_edge(self, v1: V, v2: V):
        if v1 in self._g:
            self._g[v1].add(v2)
        else:
            self._g[v1] = set([v2])
        if not self._info["Directed"]:
            if v2 in self._g:
                self._g[v2].add(v1)
            else:
                self._g[v2] = set([v1])

    def delete_vertx(self, x: V):
        if x not in self._g:
            return
        for i in self._g.keys():
            self._g[i].discard(x)
        del self._g[x]

    def delete_edge(self, v1: V, v2: V):
        if v1 in self._g[v2]:
            self._g[v2].discard(v1)
        if not self._info["Directed"]:
            if v2 in self._g[v1]:
                self._g[v1].discard(v2)

    def bfs(self, root: V, func: Callable):
        visited = []
        queue = Queue(len(self._g))
        queue.put(root)
        while not queue.empty():
            c = queue.get()
            if c in visited:
                continue
            else:
                func(c)
                visited.append(c)
            for i in self._g[c]:
                if i not in visited:
                    queue.put(i)

    def dfs(self, root: V, func: Callable):
        visited = []
        stack = LifoQueue(len(self._g))
        stack.put(root)
        while not stack.empty():
            c = stack.get()
            if c in visited:
                continue
            else:
                func(c)
                visited.append(c)
            for i in self._g[c]:
                if i not in visited:
                    stack.put(i)

    def dijkstra(self, root: V) -> dict:
        distance_table = {}
        visited = []
        for i in self._g.keys():
            distance_table[i] = {}
        queue = PriorityQueue(len(self._g))
        queue.put((0, root))
        while not queue.empty():
            _, c = queue.get()
            if c in visited:
                continue
            else:
                visited.append(c)
            for i in self._g[c]:
                if i not in visited:
                    if "distance" in distance_table[c]:
                        distance = distance_table[c]["distance"] + 1
                    else:
                        distance = 1
                    distance_table[i] = {
                        "distance": distance,
                        "from": c
                    }
                    queue.put((distance, i))
        return distance_table

    def get_info(self) -> dict:
        self._info["Vertx"] = len(self._g.keys())
        self._info["Edges"] = None
        return self._info
