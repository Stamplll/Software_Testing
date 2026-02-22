def gridChallenge(grid):
    # sort each row
    grid = [''.join(sorted(row)) for row in grid]

    rows = len(grid)
    cols = len(grid[0])   

    for row in range(rows - 1):
        for col in range(cols):
            if grid[row][col] > grid[row + 1][col]:
                return "NO"

    return "YES"

# if __name__ == '__main__':
#     t = int(input())
#     for _ in range(t):
#         n = int(input())
#         grid = []

#         for _ in range(n):
#             grid.append(input())

#         print(gridChallenge(grid))