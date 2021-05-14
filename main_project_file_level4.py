# importing libraries that might and might not have a potential usage in the program
import turtle                    # import turtle library
import time
import sys
import tkinter

# defining global variables to be used for all levels
global frame
global begin_x
global begin_y
global finish_x
global finish_y
global turtle_current_x
global turtle_current_y

# defining a function call for one of the levels of the main project, the number of the level might change depending on the difficulty of the other levels


def level_4():
    # A dictionary to keep a record of visited pixels when running BFS on our maze
    pixels_visited = {}
    path = []  # list of nodes to be visited during BFS search
    queue = []  # this list keeps the record of next node to be visited
    visited = []  # keeps record of the visited nodes so that they should not be visited again
    # defining the main turtle screen using turtle library
    window = turtle.Screen()
    window.delay(0)  # a helpful function for faster execution
    # the background of main window is defined as black
    window.bgcolor("#00bfff")
    window.title("Level 2")  # tentative window name
    window.setup(660, 650)  # window dimensions to suit the size of maze

    # this function creates the walls of the maze and assigns the pixels of the paths that can be visited by the player
    def create_maze_level_4(frame):
        global begin_x, begin_y, finish_x, finish_y
        # defining a turtle's specifications to create the walls of our maze
        maze = turtle.Turtle()
        maze.shape('square')
        maze.color('#00008b')
        # the size helps us to fit the maze within the window frame
        maze.shapesize(0.49,0.49,0.49)
        maze.penup()  # this hides the working of turtle in background from the user
        maze.speed(0)  # hides the moving turtle across the screen
        # iterating over the rows and columns of our frame to visit each and every character
        for y in range(len(frame)):
            for x in range(len(frame[y])):
                character = frame[y][x]
                # these variables defines the pixel on the screen where the program will start drawing its maze from
                screen_x = -296 + (x * 10)
                screen_y = 308 - (y * 10)
                # creating walls for our maze
                if character == "+":
                    maze.goto(screen_x, screen_y)
                    maze.stamp()
                # recording paths to be visited
                if character == " " or character == "e" or character == "s":
                    path.append((screen_x, screen_y))
                # assigning a turtle to signify our starting point
                if character == "e":
                    start = turtle.Turtle()
                    start.shape('square')
                    start.color('#b0e0e6')
                    start.shapesize(0.49,0.49,0.49)
                    start.penup()
                    start.speed(0)
                    start.goto(screen_x, screen_y)
                    start.stamp()
                    finish_x, finish_y = screen_x, screen_y
                # assigning a turtle to signify our end point
                if character == "s":
                    end = turtle.Turtle()
                    end.shape('square')
                    end.color('#b0e0e6')
                    end.shapesize(0.49,0.49,0.49)
                    end.penup()
                    end.speed(0)
                    end.goto(screen_x, screen_y)
                    end.stamp()
                    begin_x, begin_y = screen_x, screen_y

    # create a function that visits all the paths and search for a path from the start of our maze to the end
    def Breadth_First_Search(x, y):
        queue.append((x, y))     # nodes are appended in the queue for bfs
        # this dictionary keeps track of pixels visited during bfs
        pixels_visited[x, y] = x, y
        # defining turtle specifications
        tracker = turtle.Turtle()
        tracker.shape('square')
        tracker.color('#4682b4')
        tracker.penup()  # hides the working of turtle in background from the user
        tracker.speed(0)  # hides the moving turtle across the screen
        # the size helps us to fit the maze within the window frame
        tracker.shapesize(0.49, 0.49, 0.49)
        while len(queue) > 0:  # while queue is not empty
            time.sleep(0)  # executes the next line of code
            x, y = queue.pop(0)  # the first element from queue is popped
            if(x - 10, y) in path and (x - 10, y) not in visited:  # check the cell left
                cell = (x - 10, y)  # coordinate for the cell left
                pixels_visited[cell] = x, y
                queue.append(cell)   # adds cell to queue list
                visited.append((x-10, y))  # adds cell to visited list
            if (x, y - 10) in path and (x, y - 10) not in visited:  # check the cell down
                cell = (x, y - 10)  # coordinate for the cell down
                pixels_visited[cell] = x, y
                queue.append(cell)  # adds cell to queue list
                visited.append((x, y - 10))  # adds cell to visited list
                # print(solution)
            if (x + 10, y) in path and (x + 10, y) not in visited:   # check the cell right
                cell = (x + 10, y)  # coordinate for the cell right
                pixels_visited[cell] = x, y
                queue.append(cell)  # adds cell to queue list
                visited.append((x + 10, y))  # adds cell to visited list
            if (x, y + 10) in path and (x, y + 10) not in visited:  # check the cell up
                cell = (x, y + 10)  # coordinate for the cell up
                pixels_visited[cell] = x, y
                queue.append(cell)  # adds cell to queue list
                visited.append((x, y + 10))  # adds cell to visited list
            tracker.goto(x, y)
            tracker.stamp()
            # use the links attached in the "project_refernce_link" file to create this function

    # traverse over all the paths found and print the path that goes from start till end only
    def back_tracking(x, y):
        back_track = turtle.Turtle()
        back_track.shape('square')
        back_track.color('#b0c4de')
        back_track.penup()
        back_track.speed(0)
        back_track.shapesize(0.49, 0.49, 0.49)
        back_track.goto(x, y)
        back_track.stamp()
        #the method below has a pre-requisite of running the BFS function first where we search for all pixels that can be visited in the pixels_visited dictionary
        # while (x, y) != (begin_x, begin_y):
        #     back_track.goto(pixels_visited[x, y])
        #     back_track.stamp()
        #     x, y = pixels_visited[x, y]
        #we instead use this alternate method where we ony run BFS once and calculate all the pixels that are there in the shortest path so that when timer gets over, the user doesnt have to wait a long time of waiting for BFS to look what the shortest path was
        # final_path=[]
        # while (x, y) != (begin_x, begin_y):
        #   x, y = pixels_visited[x, y]
        #   final_path.append((x,y))
        # print(final_path)
        #using the solution above we print the final path in the terminal and then copy the solution into a final_path variable
        final_path=[(294, -282), (284, -282), (274, -282), (264, -282), (254, -282), (244, -282), (234, -282), (224, -282), (214, -282), (204, -282), (194, -282), (184, -282), (174, -282), (164, -282), (164, -272), (164, -262), (164, -252), (164, -242), (164, -232), (164, -222), (154, -222), (144, -222), (144, -232), (144, -242), (144, -252), (144, -262), (144, -272), (134, -272), (124, -272), (114, -272), (104, -272), (104, -262), (104, -252), (104, -242), (104, -232), (104, -222), (94, -222), (84, -222), (84, -232), (84, -242), (84, -252), (84, -262), (84, -272), (74, -272), (64, -272), (54, -272), (44, -272), (34, -272), (24, -272), (14, -272), (4, -272), (-6, -272), (-16, -272), (-16, -262), (-16, -252), (-26, -252), (-36, -252), (-46, -252), (-56, -252), (-66, -252), (-76, -252), (-86, -252), (-96, -252), (-96, -242), (-96, -232), (-96, -222), (-96, -212), (-86, -212), (-76, -212), (-76, -202), (-76, -192), (-86, -192), (-96, -192), (-96, -182), (-96, -172), (-96, -162), (-96, -152), (-86, -152), (-76, -152), (-76, -142), (-76, -132), (-86, -132), (-96, -132), (-106, -132), (-106, -122), (-106, -112), (-106, -102), (-116, -102), (-126, -102), (-136, -102), (-136, -92), (-136, -82), (-136, -72), (-136, -62), (-136, -52), (-136, -42), 
(-146, -42), (-156, -42), (-166, -42), (-176, -42), (-186, -42), (-186, -32), (-186, -22), (-186, -12), (-186, -2), (-186, 8), (-186, 18), (-176, 18), (-166, 18), (-166, 8), (-166, -2), (-166, -12), (-156, -12), (-146, -12), (-136, -12), (-126, -12), (-116, -12), (-106, -12), (-106, -22), (-106, -32), (-106, -42), (-96, -42), (-86, -42), (-76, -42), (-76, -52), (-76, -62), (-76, -72), (-66, -72), (-56, -72), (-46, -72), (-46, -82), (-46, -92), (-46, -102), (-46, -112), (-46, -122), (-36, -122), (-26, -122), (-16, -122), (-16, -112), (-16, -102), (-16, -92), (-6, -92), (4, -92), (14, -92), (14, -82), (14, -72), (4, -72), (-6, -72), (-16, -72), (-16, -62), (-16, -52), (-16, -42), (-26, -42), (-36, -42), (-46, -42), (-46, -32), (-46, -22), (-46, -12), (-56, -12), (-66, -12), (-76, -12), (-76, -2), (-76, 8), (-76, 18), (-86, 18), (-96, 18), (-106, 18), (-116, 18), (-126, 18), 
(-136, 18), (-136, 28), (-136, 38), (-136, 48), (-136, 58), (-136, 68), (-136, 78), (-146, 78), (-156, 78), (-156, 88), (-156, 98), (-156, 108), (-156, 118), (-146, 118), (-136, 118), (-126, 118), (-116, 118), (-106, 118), (-106, 128), (-106, 138), (-116, 138), (-126, 138), (-136, 138), (-146, 138), (-156, 138), (-166, 138), (-166, 148), (-166, 158), (-166, 168), (-176, 168), (-186, 168), (-196, 168), (-206, 168), (-216, 168), (-216, 158), (-216, 148), (-216, 138), (-216, 128), (-216, 118), (-226, 118), (-236, 118), (-246, 118), (-256, 118), (-256, 128), (-256, 138), (-256, 148), (-256, 158), (-256, 168), (-256, 178), (-256, 188), (-256, 198), (-256, 208), (-256, 218), (-256, 228), (-266, 228), (-276, 228), (-286, 228), (-286, 238), (-286, 248), (-286, 258), (-286, 268), (-286, 278), (-286, 288), (-286, 298), (-296, 298)]
        for i in final_path:
           back_track.goto(i)
           back_track.stamp()
    frame = ['+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++',
             's        +     +     +        +        +     +        +     +',
             '+        +     +     +        +        +     +        +     +',
             '+  ++++  +  +  +  +  ++++  +  ++++  +  +  +  +  ++++  +  ++++',
             '+  +     +  +     +        +     +  +     +  +  +     +     +',
             '+  +     +  +     +        +     +  +     +  +  +     +     +',
             '+  ++++  +  +++++++++++++++++++  +  +++++++  +  +  +++++++  +',
             '+     +     +           +        +     +     +  +        +  +',
             '+     +     +           +        +     +     +  +        +  +',
             '+  +  +++++++  +  +++++++  ++++++++++  +  ++++  +++++++  +  +',
             '+  +  +        +     +     +        +  +        +     +     +',
             '+  +  +        +     +     +        +  +        +     +     +',
             '+  +  ++++++++++  +  +  ++++  ++++  +  ++++  ++++  +  +++++++',
             '+  +  +        +  +     +     +  +  +     +  +     +        +',
             '+  +  +        +  +     +     +  +  +     +  +     +        +',
             '+  +  +  ++++  +++++++  +  +  +  +  ++++  +  +  ++++++++++  +',
             '+  +  +  +  +        +  +  +  +           +  +  +     +     +',
             '+  +  +  +  +        +  +  +  +           +  +  +     +     +',
             '+  +  +  +  +++++++  +  ++++  +++++++++++++  +  +  +  +  +  +',
             '+  +     +  +        +     +        +        +  +  +  +  +  +',
             '+  +     +  +        +     +        +        +  +  +  +  +  +',
             '+  +++++++  +  ++++++++++  +++++++  +  +++++++  ++++  +  ++++',
             '+           +     +     +     +     +  +              +     +',
             '+           +     +     +     +     +  +              +     +',
             '++++++++++  ++++  +  +++++++  +  ++++  +  ++++++++++++++++  +',
             '+              +  +           +  +     +  +     +           +',
             '+              +  +           +  +     +  +     +           +',
             '+  +++++++++++++  +++++++  ++++  +++++++  +  ++++  ++++++++++',
             '+  +     +     +        +     +        +  +     +  +  +     +',
             '+  +     +     +        +     +        +  +     +  +  +     +',
             '+  ++++  +  +  +++++++  ++++  +++++++  +  ++++  ++++  +  +  +',
             '+     +  +  +        +     +        +  +     +     +     +  +',
             '+     +  +  +        +     +        +  +     +     +     +  +',
             '++++  +  +  +++++++  ++++  +++++++  +  ++++  ++++  +  ++++  +',
             '+     +  +        +     +     +     +     +     +        +  +',
             '+     +  +        +     +     +     +     +     +        +  +',
             '+  ++++  +++++++  ++++  ++++  ++++  ++++  ++++  +  +++++++  +',
             '+     +        +  +        +     +        +  +  +  +        +',
             '+     +        +  +        +     +        +  +  +  +        +',
             '++++  +  ++++  +  +++++++  ++++  +++++++  +  +  ++++  +++++++',
             '+  +  +     +  +     +     +     +  +        +     +        +',
             '+  +  +     +  +     +     +     +  +        +     +        +',
             '+  +  +  +  +  ++++  ++++  +  ++++  +  ++++++++++  +++++++  +',
             '+     +  +  +  +  +     +     +     +  +  +     +        +  +',
             '+     +  +  +  +  +     +     +     +  +  +     +        +  +',
             '+  +++++++  +  +  ++++  ++++++++++  +  +  +  +  +++++++  +  +',
             '+           +     +     +           +  +  +  +        +  +  +',
             '+           +     +     +           +  +  +  +        +  +  +',
             '++++++++++++++++  +  +++++++  +++++++  +  +  +++++++  +  +  +',
             '+     +        +  +     +     +           +        +     +  +',
             '+     +        +  +     +     +           +        +     +  +',
             '+  +  +  +  +  +  ++++  +  ++++  ++++++++++++++++  +++++++  +',
             '+  +     +  +  +  +     +        +  +     +     +        +  +',
             '+  +     +  +  +  +     +        +  +     +     +        +  +',
             '+  +++++++  ++++  +  ++++++++++  +  +  +  +  +  +++++++  +  +',
             '+     +  +     +  +           +     +  +  +  +        +     +',
             '+     +  +     +  +           +     +  +  +  +        +     +',
             '++++  +  ++++  +  ++++++++++  +++++++  +  +  +  ++++++++++  +',
             '+           +              +           +     +              +',
             '+           +              +           +     +              e',
             '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++']  # define a maze for our level
    #we use this function to find the coordinates of the screen to start creating the maze from those coordinates so that it fits the screen size
    # def buttonclick(x,y): 
    #     print("You clicked at this coordinate({0},{1})".format(x,y))
  
    # #onscreen function to send coordinate
    # turtle.onscreenclick(buttonclick,1) 
    # turtle.listen()  # listen to incoming connections
    # turtle.speed(10) # set the speed
    # turtle.done()    # hold the screen

    # calling all the functions within our main function
    create_maze_level_4(frame)
    #we comment out the BFS function once we have completed all steps to generate the final path
    # Breadth_First_Search(begin_x, begin_y)
    # back_tracking(finish_x, finish_y)

    #now we will create functions for our player to move the turtle
    start = (begin_x, begin_y)      #this records the coordinates of our destination point on screen
    #creating a function to move our turtle forward in the y direction
    def forward():
        # uses positive y-axis value to move the turtle up by the use of 'Up' arrow key
        global turtle_current_y
        # as the turtle moves up, 'y' values change while 'x' values remain constant
        new_coordinates = (turtle_current_x, turtle_current_y + 10)
        if new_coordinates == start:  # if the turtle reaches start value, then reset screen
            window.resetscreen()
        if (new_coordinates in path):
            # checks if the new cordinate is not in the restricted path i.e. outside the walls, then move the turtle one step up.
            turtle_current_y += 10
            # goes back and stamps colour where the turtle previously stood to keep track of where the user is moving.
            turtle.goto(turtle_current_x, turtle_current_y)
            turtle.stamp()

    # Back
    def backward():
        # uses negative y-axis value to move the turtle down by the use of 'Down' arrow key
        global turtle_current_y
        # as the turtle moves down, 'y' values change while 'x' values remain constant
        new_coordinates = (turtle_current_x, turtle_current_y - 10)
        if new_coordinates == start:  # if the turtle reaches start value, then reset screen
            window.resetscreen()
        if (new_coordinates in path):
            # checks if the new cordinate is not in the restricted path i.e. outside the walls, then move the turtle one step down.
            turtle_current_y -= 10
            # goes back and stamps colour where the turtle previously stood to keep track of where the user is moving.
            turtle.goto(turtle_current_x, turtle_current_y)
            turtle.stamp()

    # Left
    def left():
        # uses negative x-axis value to move the turtle down by the use of 'Left' arrow key
        global turtle_current_x
        # as the turtle moves to the left, 'x' values change while 'y' values remain constant
        new_coordinates = (turtle_current_x - 10, turtle_current_y)
        if new_coordinates == start:  # if the turtle reaches start value, then reset screen
            window.resetscreen()
        if (new_coordinates in path):
            # checks if the new cordinate is not in the restricted path i.e. outside the walls, then move the turtle one step left.
            turtle_current_x -= 10
            turtle.goto(turtle_current_x, turtle_current_y)
            # goes back and stamps colour where the turtle previously stood to keep track of where the user is moving.
            turtle.stamp()

    # Right
    def right():
        # uses positive x-axis value to move the turtle down by the use of 'Left' arrow key
        global turtle_current_x
        # as the turtle moves to the right, 'x' values change while 'y' values remain constant
        new_coordinates = (turtle_current_x + 10, turtle_current_y)
        if new_coordinates == start:  # if the turtle reaches start value, then reset screen
            window.resetscreen()
        if (new_coordinates in path):
            # checks if the new cordinate is not in the restricted path i.e. outside the walls, then move the turtle one step right.
            turtle_current_x += 10
            turtle.goto(turtle_current_x, turtle_current_y)
            # goes back and stamps colour where the turtle previously stood to keep track of where the user is moving.
            turtle.stamp()

    # Turtle Properties
    t = turtle.Turtle()
    turtle.shapesize(0.49, 0.49, 0.49)
    turtle.penup()
    turtle.speed(0)
    turtle.setheading(90)

    # Starting position
    global turtle_current_x
    global turtle_current_y
    turtle_current_x = finish_x
    turtle_current_y = finish_y
    turtle.goto(turtle_current_x, turtle_current_y)

    # Listeners and events by user
    turtle.onkey(forward, 'Up')
    turtle.onkey(backward, 'Down')
    turtle.onkey(left, 'Left')
    turtle.onkey(right, 'Right')
    turtle.shape("square")
    turtle.color("#b0e0e6")
    turtle.listen()

    window.exitonclick()  # exits window on click


# calling our main function
level_4()