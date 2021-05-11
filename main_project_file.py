#importing libraries that might and might not have a potential usage in the program
import turtle                    # import turtle library
import time
import sys
import tkinter

#defining global variables to be used for all levels
global frame
global begin_x
global begin_y
global finish_x
global finish_y

#defining a function call for one of the levels of the main project, the number of the level might change depending on the difficulty of the other levels
def level_2():
    pixels_visited = {}         #A dictionary to keep a record of visited pixels when running BFS on our maze       
    path = []           #list of nodes to be visited during BFS search
    queue = []          #this list keeps the record of next node to be visited
    visited = []        #keeps record of the visited nodes so that they should not be visited again
    window = turtle.Screen()         # defining the main turtle screen using turtle library
    window.delay(0)         #a helpful function for faster execution
    window.bgcolor("black")         #the background of main window is defined as black
    window.title("Level 2")         #tentative window name
    window.setup(1300, 700)         #window dimensions to suit the size of maze

    #this function creates the walls of the maze and assigns the pixels of the paths that can be visited by the player
    def create_maze_level_2(frame):
        global begin_x, begin_y, finish_x, finish_y
        #defining a turtle's specifications to create the walls of our maze
        maze = turtle.Turtle()
        maze.shape('square')
        maze.color('magenta')
        maze.shapesize(1, 1, 1)     #the size helps us to fit the maze within the window frame
        maze.penup()            #this hides the working of turtle in background from the user
        maze.speed(0)           #hides the moving turtle across the screen
        #iterating over the rows and columns of our frame to visit each and every character
        for y in range(len(frame)):
            for x in range(len(frame[y])):
                character = frame[y][x]
                #these variables defines the pixel on the screen where the program will start drawing its maze from
                screen_x = -731 + (x * 18)
                screen_y = 375 - (y * 18)
                #creating walls for our maze
                if character == "+":
                    maze.goto(screen_x, screen_y)
                    maze.stamp()
                #recording paths to be visited 
                if character == " " or character == "e" or character == "s":
                    path.append((screen_x, screen_y))
                #assigning a turtle to signify our starting point
                if character == "e":
                    start = turtle.Turtle()
                    start.shape('square')
                    start.color('yellow')
                    start.shapesize(1, 1, 1)
                    start.penup()
                    start.speed(0)
                    start.goto(screen_x, screen_y)
                    start.stamp()
                    finish_x, finish_y = screen_x, screen_y
                #assigning a turtle to signify our end point
                if character == "s":
                    end = turtle.Turtle()
                    end.shape('square')
                    end.color('orange')
                    end.shapesize(1, 1, 1)
                    end.penup()
                    end.speed(0)
                    end.goto(screen_x, screen_y)
                    end.stamp()
                    begin_x, begin_y = screen_x, screen_y
    
    #create a function that visits all the paths and search for a path from the start of our maze to the end
    def Breadth_First_Search(x, y):
    queue.append((x, y))     # nodes are appended in the queue for bfs 
    pixels_visited[x, y] = x, y  #this dictionary keeps track of pixels visited during bfs
    #defining turtle specifications 
    tracker = turtle.Turtle() 
    tracker.shape('square')
    tracker.color('black')
    tracker.penup() #hides the working of turtle in background from the user
    tracker.speed(0) #hides the moving turtle across the screen
    tracker.shapesize(1, 1, 1) #the size helps us to fit the maze within the window frame
    while len(queue) > 0: #while queue is not empty 
        time.sleep(0) #executes the next line of code 
        x,y = queue.pop(0) #the first element from queue is popped
        if(x - 18, y) in path and (x - 18, y) not in visited: #check the cell left 
                cell = (x - 18, y) #coordinate for the cell left
                pixels_visited[cell] = x, y
                queue.append(cell)   # adds cell to queue list
                visited.append((x-18, y))  # adds cell to visited list
            if (x, y - 18) in path and (x, y - 18) not in visited:  # check the cell down
                cell = (x, y - 18) #coordinate for the cell down
                pixels_visited[cell] = x, y
                queue.append(cell) # adds cell to queue list
                visited.append((x, y - 14.5)) # adds cell to visited list
                # print(solution)
            if (x + 18, y) in path and (x + 18, y) not in visited:   # check the cell right
                cell = (x + 18, y) #coordinate for the cell right
                pixels_visited[cell] = x, y
                queue.append(cell) # adds cell to queue list
                visited.append((x + 18, y)) # adds cell to visited list
            if (x, y + 18) in path and (x, y + 18) not in visited:  # check the cell up
                cell = (x, y + 18) #coordinate for the cell up
                pixels_visited[cell] = x, y
                queue.append(cell) # adds cell to queue list
                visited.append((x, y + 18)) # adds cell to visited list
            tracker.goto(x, y)
            tracker.stamp()
        #use the links attached in the "project_refernce_link" file to create this function

    #traverse over all the paths found and print the path that goes from start till end only
    def back_tracking(x, y):
        pass
        #use the links attached in the "project_refernce_link" file to create this function

    frame=[]        #define a maze for our level

    #calling all the functions within our main function
    create_maze_level_2(frame)
    Breadth_First_Search(begin_x, begin_y)
    back_tracking(finish_x, finish_y)
    window.exitonclick()

#calling our main function
level_2()
