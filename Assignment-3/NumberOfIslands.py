# Given a binary matrix in which 1s represent land and 0s represent water.
# Return the number of islands (contiguous 1s surrounded by 0s or the edge of the matrix).
# time complexity O(m * n), m, n refer to the number of row and col of the matrix
# space complexity O(m * n), m, n refer to the number of row and col of the matrix
# time spent on the question: about 40 min
from collections import deque


def bfs(source, matrix, visited):
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque()
    queue.append(source)
    row = len(matrix)
    col = len(matrix[0])
    while len(queue) > 0:
        current = queue.popleft()
        visited.add(current)
        for i, j in direction:
            x, y = current[0] + i, current[1] + j
            if 0 <= x < row and 0 <= y < col and matrix[x][y] == 1 and (x, y) not in visited:
                queue.append((x, y))


def NumberOfIslands(matrix):
    visited = set()  # use a set to keep track of visited position
    num_island = 0
    row = len(matrix)
    col = len(matrix[0])
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 1 and (i, j) not in visited:
                # using bfs to find an island
                bfs((i, j), matrix, visited)
                num_island += 1
    return num_island


if __name__ == "__main__":
    input_matrix = [[1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 0]]
    print(NumberOfIslands(input_matrix))
