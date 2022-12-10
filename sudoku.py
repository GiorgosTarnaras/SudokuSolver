import numpy as np

def main():
    myGrid = [[0,0,0,2,7,3,9,0,5],
       [5,0,0,0,0,9,0,3,7],
       [7,9,0,4,0,0,0,0,2],
       [0,8,0,5,2,6,4,0,0],
       [1,6,5,8,0,0,0,0,0],
       [0,0,2,0,9,0,5,0,6],
       [0,0,1,0,0,5,3,6,0],
       [9,3,8,0,6,2,0,0,0],
       [0,0,0,9,3,0,0,2,8]]

    while not check_solved(myGrid): solve_grid(myGrid)
    print(np.array(myGrid))

def check_solved(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:return False

    return True

def check_cell(row, col, box):
    numbers = set(row + col + box)
    if len(numbers) == 9:
        for i in range(1, 10):
            if i not in numbers: return i
    else: return 0

def solve_grid(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                grid[i][j] = check_cell(grid[i], getCol(grid, j), getBox(grid, i, j))

def getCol(grid, j):
    nums = []
    for i in range(9):
        nums.append(grid[i][j])
    return nums

def getBox(grid, i, j):
    nums = []
    for m in range(i-i%3,i-i%3+3):
        for n in range(j-j%3,j-j%3+3):
            nums.append(grid[m][n])
    return nums

if __name__ == "__main__":
    main()