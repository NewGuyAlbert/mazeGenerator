import random
from random import randrange

class Maze:
    def __init__(self, size):
        #Size represents n x n of rows and columns
        self.size = size
        #The maze is represented by grid as a 2 dimensional list
        self.grid = self.createGrid()
        #WallsList will contain cells (that are walls) that will later become paths or remain as walls
        self.wallsList = []
        #Starting position
        self.start = 0
        #Finish position
        self.finish = 0
    
    def __call__(self):
        self.printMaze()

    #Creates a grid full of walls
    def createGrid(self):
        grid = [[-1 for col in range(self.size)] for row in range(self.size)]
        return grid

    #Makes the center of the grid into a path and takes care of making the maze from there
    
    def createMaze(self):
        # The variable c represents the center of the grid
        c = self.size//2
        self.grid[c][c] = 0
        self.addToWallsList([c,c])

        while(len(self.wallsList) > 0):
            self.makePath(random.choice(self.wallsList))

        #Set Start
        while True:
            self.start = self.pickRandomPosition()
            if self.grid[self.start[0]][self.start[1]] == 0:
                break
        #Set finish
        while True:
            self.finish = self.pickRandomPosition()
            if self.grid[self.finish[0]][self.finish[1]] == 0:
                break
    
    #Tests if the given wall should become a path or stay a wall
    def makePath(self,wall):
        row = wall[0]
        col = wall[1]
        
        try:
            if(row != 0 and col != 0):
                if((self.grid[row-1][col] + self.grid[row][col+1] + self.grid[row+1][col] + self.grid[row][col-1]) == -3):
                    self.grid[row][col] = 0 #The wall becomes path
                    self.addToWallsList([row,col])
        except IndexError:
            pass

        self.wallsList.remove(wall)

    #Ads the walls of the given path to the WallsList
    def addToWallsList(self,path):
        row = path[0]
        col = path[1]

        if(self.grid[row-1][col] == -1):
            self.wallsList.append([row-1,col])
        if(self.grid[row][col+1] == -1):
            self.wallsList.append([row,col+1])
        if(self.grid[row+1][col] == -1):
            self.wallsList.append([row+1,col])
        if(self.grid[row][col-1] == -1):
            self.wallsList.append([row,col-1])

    #Picks a random position from the grid
    def pickRandomPosition(self):
        return randrange(self.size),randrange(self.size)

    #Prints the maze with the values -1 and 0
    def printMaze(self):
        for row in self.grid:
            for val in row:
                print(val, end=" ")
            print()
    
    #Prints the maze with the values '#' and ' '
    def printPrettyMaze(self):
        for row in self.grid:
            for val in row:
                if val == 0:
                    print(" ", end=" ")
                else:
                    print("#", end="")
            print()

