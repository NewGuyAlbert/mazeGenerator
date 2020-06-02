import random
from random import randrange

class MazeSolver:
    def __init__(self, size, grid, start, finish):
        #Size represents n x n of rows and columns
        self.size = size
        #The maze is represented by grid as a 2 dimensional list
        self.grid = grid.copy()
        #Maze starting point
        self.start = start
        #Maze finish point
        self.finish = finish
        #Boolean that turns true when maze is solved
        self.solved = False
        #The cells that form the shortest route from start to finish will be stored in the path variable
        self.path = []

    def solveMaze(self):
        self.incrementNeighbours(self.start,0)
        #cellValue represent the value a cell needs to have in order for its neigbours to be incremented
        cellValue = 1
        while(not self.solved):
            self.incrementMaze(cellValue)
            cellValue += 1
        
        #After the maze is solved we reverse the path so the elements are from start to finish and not from finish to start
        self.path.reverse()
        

    def incrementMaze(self,value):
        for i, row in  enumerate(self.grid):
            for j, val in enumerate(row):
                if self.solved is True:
                    break
                if val == value:
                    cell = [i,j]
                    try:
                        if(i != 0 and j != 0):
                            self.incrementNeighbours(cell,value)
                    except IndexError:
                        pass

    def incrementNeighbours(self,cell,value):
        row = cell[0]
        col = cell[1]

        #TODO This method is ugly, make pretty
        if(row-1 != 0):
            if(self.grid[row-1][col] == -3):
                self.makePath([row-1, col], value + 1)
                self.solved = True
            elif(self.grid[row-1][col] == 0):
                self.grid[row-1][col] = value + 1

        if(col+1 != self.size-1 and self.solved == False):
            if(self.grid[row][col+1] == -3):
                self.makePath([row, col+1], value + 1)
                self.solved = True
            elif(self.grid[row][col+1] == 0):
                self.grid[row][col+1] = value + 1

        if(row+1 != self.size-1 and self.solved == False):
            if(self.grid[row+1][col] == -3):
                self.makePath([row+1, col], value + 1)
                self.solved = True
            elif(self.grid[row+1][col] == 0):
                self.grid[row+1][col] = value + 1

        if(col-1 != 0 and self.solved == False):
            if(self.grid[row][col-1] == -3):
                self.makePath([row, col-1], value + 1)
                self.solved = True
            elif(self.grid[row][col-1] == 0):
                self.grid[row][col-1] = value + 1

    def makePath(self,cell,distance):
        while(distance):
            self.path.append(cell)
            distance -= 1
            cell = self.findNextCell(cell,distance)
    
    def findNextCell(self,cell,distance):
        row = cell[0]
        col = cell[1]

        try:
            if(row-1 != 0):
                if(self.grid[row-1][col] == distance):
                    return [row-1, col]

            if(col+1 != self.size-1):
                if(self.grid[row][col+1] == distance):
                    return [row, col+1]
                

            if(row+1 != self.size-1):
                if(self.grid[row+1][col] == distance):
                    return [row+1, col]
                

            if(col-1 != 0):
                if(self.grid[row][col-1] == distance):
                    return [row, col-1]
                        
        except IndexError:
            pass
    #Prints the maze with the values -1 and 0
    def printMaze(self):
        for row in self.grid:
            for val in row:
                print(val, end=" ")
            print()