# Given a binary matrix in which 1s represent land and 0s represent water.
# Return the number of islands (contiguous 1s surrounded by 0s or the edge of the matrix).
# time complexity O(m * n), m, n refer to the number of row and col of the matrix
# space complexity O(m * n), m, n refer to the number of row and col of the matrix
# time spent on the question: about 20 min
from collections import deque


def NumberOfIslands(matrix):
    visited = set()  # use a set to keep track of visited position
    num_island = 0
    row = len(matrix)
    col = len(matrix[0])
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 1 and (i, j) not in visited:
                # using bfs to find an island
                index_queue = deque()
                index_queue.append((i, j))
                while len(index_queue) > 0:
                    size = len(index_queue)
                    for num in range(size):
                        x, y = index_queue.popleft()
                        visited.add((x, y))
                        direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # 4 possible directions
                        for l, r in direction:
                            if 0 <= x + l < row and 0 <= y + r < col:
                                if matrix[x + l][y + r] == 1 and (x + l, y + r) not in visited:
                                    index_queue.append((x + l, y + r))
                num_island += 1
    return num_island


if __name__ == "__main__":
    input_matrix = [[1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 0]]
    print(NumberOfIslands(input_matrix))
