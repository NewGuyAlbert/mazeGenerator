from tkinter import *
from maze import Maze

if __name__ == "__main__":
    #Create maze object
    maze = Maze(40)
    maze.createMaze()
    
    #Create GUI object
    root = Tk()
    root.geometry("1000x1000")
    Grid.rowconfigure(root, 0, weight=1)
    Grid.columnconfigure(root, 0, weight=1)

    #Create & Configure frame 
    frame=Frame(root)
    frame.grid(row=0, column=0, sticky=N+S+E+W)

    #Create the grid of buttons inside the frame
    for i in range(0,maze.size):
        Grid.rowconfigure(frame, i, weight=1)
        for j in range(0,maze.size):
            if(maze.grid[i][j] == -1):
                Grid.columnconfigure(frame, j, weight=1)
                btn = Button(frame, bg = 'black') #create a button inside frame 
                btn.grid(row=i, column=j, sticky=N+S+E+W)  
            else:
                Grid.columnconfigure(frame, j, weight=1)
                btn = Button(frame, activebackground='black') #create a button inside frame 
                btn.grid(row=i, column=j, sticky=N+S+E+W)  
    
    #Put the start button
    btn = Button(frame, bg = 'green') #create a button inside frame 
    btn.grid(row=maze.start[0], column=maze.start[1], sticky=N+S+E+W)  

    #Put the finish button
    btn = Button(frame, bg = 'red') #create a button inside frame 
    btn.grid(row=maze.finish[0], column=maze.finish[1], sticky=N+S+E+W)  

    root.mainloop()
