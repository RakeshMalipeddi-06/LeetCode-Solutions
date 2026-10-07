from collections import deque

class Solution(object):
    def nearestExit(self, maze, entrance):
        rows = len(maze)
        cols = len(maze[0])

        start_r, start_c = entrance

        q = deque([(start_r, start_c)])

        visited = set()
        visited.add((start_r, start_c))

        distance = 0

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        while q:

            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (0 <= nr < rows and
                        0 <= nc < cols and
                        (nr, nc) not in visited and
                        maze[nr][nc] == "."):

                        if ((nr == 0 or nr == rows - 1 or
                             nc == 0 or nc == cols - 1)
                            and (nr, nc) != (start_r, start_c)):
                            return distance + 1

                        visited.add((nr, nc))
                        q.append((nr, nc))

            distance += 1

        return -1

