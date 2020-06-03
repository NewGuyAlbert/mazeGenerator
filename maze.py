import random
from random import randrange

#Config variables
#Please choose value from 1 to 100 (1 means there will always be just one path from start to finish, while 100 will remove as many walls as possible to make sure there are multiple paths from start to finish)
PERCENTAGE = 1
#Boolean that determines if the start and finish will be chosen randomly or will be in opposite cornes from each other
FIXEDSTART = True


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

        if(not FIXEDSTART):
            #Set Start
            while True:
                self.start = self.pickRandomPosition()
                if self.grid[self.start[0]][self.start[1]] == 0:
                    #We make the value of the start -2
                    self.grid[self.start[0]][self.start[1]] = -2
                    break
            #Set Finish
            while True:
                self.finish = self.pickRandomPosition()
                if self.grid[self.finish[0]][self.finish[1]] == 0:
                    #We make the value of the finish = -3
                    self.grid[self.finish[0]][self.finish[1]] = -3
                    break
        else:
            #Set Start
            i,j = 1,1
            while True:
                self.start = [i,j]
                if self.grid[self.start[0]][self.start[1]] == 0:
                    #We make the value of the start -2
                    self.grid[self.start[0]][self.start[1]] = -2
                    break
                if(i >= j):
                    j += 1
                else:
                    i += 1

            #Set Finish
            i,j = self.size-1,self.size-1
            while True:
                self.finish = [i,j]
                if self.grid[self.finish[0]][self.finish[1]] == 0:
                    #We make the value of the finish = -3
                    self.grid[self.finish[0]][self.finish[1]] = -3
                    break
                if(i <= j):
                    j -= 1
                else:
                    i -= 1
                

    
    #Tests if the given wall should become a path or stay a wall
    def makePath(self,wall):
        row = wall[0]
        col = wall[1]
        
        try:
            if(row != 0 and col != 0):

                #Roll random number for the elif (This number will represent the percentage that determines how often the maze will have more than one path going from a random point a to a random point b)
                roll = random.randint(1,100)

                if((self.grid[row-1][col] + self.grid[row][col+1] + self.grid[row+1][col] + self.grid[row][col-1]) == -3):
                    self.grid[row][col] = 0 #The wall becomes path
                    self.addToWallsList([row,col])
                elif((self.grid[row-1][col] + self.grid[row][col+1] + self.grid[row+1][col] + self.grid[row][col-1]) == -2 and roll <= PERCENTAGE):
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

    #Prints the maze with numeric values
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


