# importing libraries that might and might not have a potential usage in the program
import turtle                    # import turtle library
import time
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


def level_2():
    # A dictionary to keep a record of visited pixels when running BFS on our maze
    pixels_visited = {}
    path = []  # list of nodes to be visited during BFS search
    queue = []  # this list keeps the record of next node to be visited
    visited = []  # keeps record of the visited nodes so that they should not be visited again
    # defining the main turtle screen using turtle library
    window = turtle.Screen()
    window.delay(0)  # a helpful function for faster execution
    # the background of main window is defined as black
    window.bgcolor("#ffd700")
    window.title("Level 2")  # tentative window name
    window.setup(1200, 610)  # window dimensions to suit the size of maze

    # this function creates the walls of the maze and assigns the pixels of the paths that can be visited by the player
    def create_maze_level_2(frame):
        global begin_x, begin_y, finish_x, finish_y
        # defining a turtle's specifications to create the walls of our maze
        maze = turtle.Turtle()
        maze.shape('square')
        maze.color('#ff4500')
        # the size helps us to fit the maze within the window frame
        maze.shapesize(0.67, 0.67, 0.67)
        maze.penup()  # this hides the working of turtle in background from the user
        maze.speed(0)  # hides the moving turtle across the screen
        # iterating over the rows and columns of our frame to visit each and every character
        for y in range(len(frame)):
            for x in range(len(frame[y])):
                character = frame[y][x]
                # these variables defines the pixel on the screen where the program will start drawing its maze from
                screen_x = -585 + (x * 14.5)
                screen_y = 295 - (y * 14.5)
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
                    start.color('#800000')
                    start.shapesize(0.67, 0.67, 0.67)
                    start.penup()
                    start.speed(0)
                    start.goto(screen_x, screen_y)
                    start.stamp()
                    finish_x, finish_y = screen_x, screen_y
                # assigning a turtle to signify our end point
                if character == "s":
                    end = turtle.Turtle()
                    end.shape('square')
                    end.color('#800000')
                    end.shapesize(0.67, 0.67, 0.67)
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
        tracker.color('#b22222')
        tracker.penup()  # hides the working of turtle in background from the user
        tracker.speed(0)  # hides the moving turtle across the screen
        # the size helps us to fit the maze within the window frame
        tracker.shapesize(0.67, 0.67, 0.67)
        while len(queue) > 0:  # while queue is not empty
            time.sleep(0)  # executes the next line of code
            x, y = queue.pop(0)  # the first element from queue is popped
            if(x - 14.5, y) in path and (x - 14.5, y) not in visited:  # check the cell left
                cell = (x - 14.5, y)  # coordinate for the cell left
                pixels_visited[cell] = x, y
                queue.append(cell)   # adds cell to queue list
                visited.append((x-14.5, y))  # adds cell to visited list
            if (x, y - 14.5) in path and (x, y - 14.5) not in visited:  # check the cell down
                cell = (x, y - 14.5)  # coordinate for the cell down
                pixels_visited[cell] = x, y
                queue.append(cell)  # adds cell to queue list
                visited.append((x, y - 14.5))  # adds cell to visited list
                # print(pixels_visited)
            if (x + 14.5, y) in path and (x + 14.5, y) not in visited:   # check the cell right
                cell = (x + 14.5, y)  # coordinate for the cell right
                pixels_visited[cell] = x, y
                queue.append(cell)  # adds cell to queue list
                visited.append((x + 14.5, y))  # adds cell to visited list
            if (x, y + 14.5) in path and (x, y + 14.5) not in visited:  # check the cell up
                cell = (x, y + 14.5)  # coordinate for the cell up
                pixels_visited[cell] = x, y
                queue.append(cell)  # adds cell to queue list
                visited.append((x, y + 14.5))  # adds cell to visited list
            tracker.goto(x, y)
            tracker.stamp()
            # use the links attached in the "project_refernce_link" file to create this function

    # traverse over all the paths found and print the path that goes from start till end only
    def back_tracking(x, y):
        back_track = turtle.Turtle()
        back_track.shape('square')
        back_track.color('#330019')
        back_track.penup()
        back_track.speed(0)
        back_track.shapesize(0.67, 0.67, 0.67)
        back_track.goto(x, y)
        back_track.stamp()
        #the method below has a pre-requisite of running the BFS function first where we search for all pixels that can be visited in the pixels_visited dictionary
        # while (x, y) != (begin_x, begin_y):
        #     back_track.goto(pixels_visited[x, y])
        #     back_track.stamp()
        #     x, y = pixels_visited[x, y]
        #we instead use this alternate method where we ony run BFS once and calculate all the pixels that are there in the shortest path so that when timer gets over, the user doesnt have to wait a long time of waiting for BFS to look what the shortest path was
        # final_path=[]
        #while (x, y) != (begin_x, begin_y):
        #   x, y = pixels_visited[x, y]
        #   final_path.append((x,y))
        #print(final_path)
        #using the solution above we print the final path in the terminal and then copy the solution into a final_path variable
        final_path = [(-5.0, -38.5), (-19.5, -38.5), (-34.0, -38.5), (-48.5, -38.5), (-48.5, -24.0), (-48.5, -9.5), (-48.5, 5.0), (-48.5, 19.5), (-63.0, 19.5), (-77.5, 19.5), (-77.5, 5.0), (-77.5, -9.5), (-92.0, -9.5), (-106.5, -9.5), (-121.0, -9.5), (-135.5, -9.5), (-135.5, 5.0), (-135.5, 19.5), (-135.5, 34.0), 
        (-135.5, 48.5), (-121.0, 48.5), (-106.5, 48.5), (-92.0, 48.5), (-77.5, 48.5), (-63.0, 48.5), (-48.5, 48.5), (-48.5, 63.0), (-48.5, 77.5), (-48.5, 92.0), (-48.5, 106.5), (-48.5, 121.0), (-48.5, 135.5), (-34.0, 135.5), (-19.5, 135.5), (-5.0, 135.5), (9.5, 135.5), (9.5, 121.0), (9.5, 106.5), (9.5, 92.0), 
        (9.5, 77.5), (9.5, 63.0), (9.5, 48.5), (24.0, 48.5), (38.5, 48.5), (53.0, 48.5), (67.5, 48.5), (82.0, 48.5), (96.5, 48.5), (111.0, 48.5), (125.5, 48.5), (125.5, 34.0), (125.5, 19.5), (125.5, 5.0), (125.5, -9.5), (125.5, -24.0), (125.5, -38.5), (140.0, -38.5), (154.5, -38.5), (169.0, -38.5), (183.5, -38.5), 
        (183.5, -24.0), (183.5, -9.5), (183.5, 5.0), (183.5, 19.5), (183.5, 34.0), (183.5, 48.5), (198.0, 48.5), (212.5, 48.5), (227.0, 48.5), (241.5, 48.5), (241.5, 63.0), (241.5, 77.5), (227.0, 77.5), (212.5, 77.5), (198.0, 77.5), (183.5, 77.5), (169.0, 77.5), (154.5, 77.5), (140.0, 77.5), (125.5, 77.5), (111.0, 77.5), 
        (96.5, 77.5), (82.0, 77.5), (67.5, 77.5), (67.5, 92.0), (67.5, 106.5), (67.5, 121.0), (67.5, 135.5), (67.5, 150.0), (67.5, 164.5), (53.0, 164.5), (38.5, 164.5), (24.0, 164.5), (9.5, 164.5), (-5.0, 164.5), (-19.5, 164.5), (-34.0, 164.5), (-48.5, 164.5), (-63.0, 164.5), (-77.5, 164.5), (-77.5, 179.0), (-77.5, 193.5), 
        (-63.0, 193.5), (-48.5, 193.5), (-48.5, 208.0), (-48.5, 222.5), (-63.0, 222.5), (-77.5, 222.5), (-92.0, 222.5), (-106.5, 222.5), (-121.0, 222.5), (-135.5, 222.5), (-135.5, 208.0), (-135.5, 193.5), (-135.5, 179.0), (-135.5, 164.5), (-150.0, 164.5), (-164.5, 164.5), (-179.0, 164.5), (-193.5, 164.5), (-193.5, 150.0), 
        (-193.5, 135.5), (-179.0, 135.5), (-164.5, 135.5), (-164.5, 121.0), (-164.5, 106.5), (-150.0, 106.5), (-135.5, 106.5), (-121.0, 106.5), (-106.5, 106.5), (-106.5, 92.0), (-106.5, 77.5), (-121.0, 77.5), (-135.5, 77.5), (-150.0, 77.5), (-164.5, 77.5), (-179.0, 77.5), (-193.5, 77.5), (-208.0, 77.5), (-222.5, 77.5), (-222.5, 92.0), 
        (-222.5, 106.5), (-237.0, 106.5), (-251.5, 106.5), (-251.5, 92.0), (-251.5, 77.5), (-251.5, 63.0), (-251.5, 48.5), (-266.0, 48.5), (-280.5, 48.5), (-295.0, 48.5), (-309.5, 48.5), (-324.0, 48.5), (-338.5, 48.5), (-353.0, 48.5), (-367.5, 48.5), (-382.0, 48.5), (-396.5, 48.5), (-411.0, 48.5), (-425.5, 48.5), (-425.5, 34.0), (-425.5, 19.5), 
        (-440.0, 19.5), (-454.5, 19.5), (-469.0, 19.5), (-483.5, 19.5), (-483.5, 5.0), (-483.5, -9.5), (-498.0, -9.5), (-512.5, -9.5), (-527.0, -9.5), (-541.5, -9.5), (-541.5, 5.0), (-541.5, 19.5), (-541.5, 34.0), (-541.5, 48.5), (-541.5, 63.0), (-541.5, 77.5), (-541.5, 92.0), (-541.5, 106.5), (-541.5, 121.0), (-541.5, 135.5), (-541.5, 150.0),
        (-541.5, 164.5), (-527.0, 164.5), (-512.5, 164.5), (-512.5, 179.0), (-512.5, 193.5), (-512.5, 208.0), (-512.5, 222.5), (-527.0, 222.5), (-541.5, 222.5), (-541.5, 237.0), (-541.5, 251.5), (-527.0, 251.5), (-512.5, 251.5), (-512.5, 266.0), (-512.5, 280.5), (-527.0, 280.5), (-541.5, 280.5), (-556.0, 280.5), (-570.5, 280.5), (-585.0, 280.5)]
        for i in final_path:
           back_track.goto(i)
           back_track.stamp()
    frame = ['+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++',
             's                       +                   +                       +           +',
             '+++++   +++++   +++++++++   +++++   +++++++++   +++++   +++++++++   +   +++++   +',
             '+       +   +   +           +   +           +       +   +   +       +       +   +',
             '+   +++++   +   +   +++++++++   +++++++++   +   +++++   +   +   +++++++++++++   +',
             '+       +       +   +                   +       +       +       +               +',
             '+   +   +   +++++   +++++   +   +++++   +++++++++   +++++++++   +++++   +++++   +',
             '+   +   +   +   +       +   +   +       +       +   +       +           +       +',
             '+++++   +   +   +++++   +++++   +   +++++++++   +   +   +   +++++++++++++   +++++',
             '+       +       +       +       +               +       +   +       +       +   +',
             '+   +   +++++++++   +++++   +++++++++++++++++   +++++++++   +++++   +   +++++   +',
             '+   +   +       +   +           +           +   +       +       +   +   +       +',
             '+   +++++   +   +   +++++++++   +++++   +   +   +   +   +++++   +   +   +   +   +',
             '+   +       +       +       +       +   +   +   +   +       +   +   +       +   +',
             '+   +   +++++++++++++   +   +++++   +   +   +   +++++++++   +   +   +++++++++   +',
             '+   +   +               +           +   +   +               +   +               +',
             '+   +   +++++++++++++   +++++++++++++   +   +++++++++++++   +   +++++++++   +++++',
             '+       +               +   +           +           +       +   +       +       +',
             '+   +++++   +++++++++++++   +   +++++++++++++++++   +   +++++   +   +   +++++   +',
             '+   +       +           +   +   +       +       +   +   +   +       +   +       +',
             '+   +   +   +   +++++   +   +   +   +   +   +   +   +   +   +++++++++   +   +++++',
             '+       +   +       +   +           +   +   +   +   +   +           +   +       +',
             '+   +++++++++++++   +   +++++++++++++   +   +   +   +   +   +++++   +   +++++   +',
             '+   +               +           +   +       +   +           +   +   +       +   +',
             '+++++   +++++++++++++++++++++   +   ++++e   +++++++++++++++++   +   +++++   +   +',
             '+   +   +       +           +   +       +   +           +       +       +   +   +',
             '+   +   +   +++++   +++++   +   +++++   +   +   +++++   +++++   +++++   +   +   +',
             '+   +   +           +       +       +       +   +           +           +   +   +',
             '+   +   +   +++++++++   ++++++++++  +   +++++   +++++++++   +++++++++   +   +++++',
             '+   +   +   +   +       +           +       +       +   +           +   +       +',
             '+   +   +   +   +   +++++   +++++++++++++++++++++   +   +++++++++   +   +++++   +',
             '+       +   +   +           +                       +               +       +   +',
             '+++++++++   +   +++++++++++++++++   +   +++++++++++++   +++++++++++++++++   +   +',
             '+       +       +               +   +       +       +           +           +   +',
             '+   +   +++++   +++++++++   +   +   +++++   +   +   +++++++++   +++++++++++++   +',
             '+   +       +       +       +   +       +   +   +   +       +           +       +',
             '+   +   +++++++++   +   +++++   +   +++++   +++++   +   +   +++++++++   +   +++++',
             '+   +           +   +   +       +   +       +       +   +           +   +       +',
             '+   +++++   +++++   +   +   +++++++++   +++++   +++++   +++++++++   +   +++++   +',
             '+       +               +               +                       +               +',
             '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++']  # define a maze for our level
    #we use this function to find the coordinates of the screen to start creating the maze from those coordinates so that it fits the screen size
    # def buttonclick(x,y): 
    #     print("You clicked at this coordinate({0},{1})".format(x,y))
  
    # #onscreen function to send coordinate
    # turtle.onscreenclick(buttonclick,1) 
    # turtle.listen()  # listen to incoming connections
    # turtle.speed(10) # set the speed
    # turtle.done()    # hold the screen
    
    # calling all the functions within our main function
    create_maze_level_2(frame)
    #we comment out the BFS function once we have completed all steps to generate the final path
    # Breadth_First_Search(begin_x, begin_y)
    # back_tracking(finish_x, finish_y)

    #now we will create functions for our player to move the turtle
    start = (begin_x, begin_y)      #this records the coordinates of our destination point on screen
    #creating a function to move our turtle forward in the y direction
    def forward():
        global turtle_current_y     #var to keep track of the coordinate where our turtle currently is
        new_coordinates = (turtle_current_x, turtle_current_y + 14.5)
        if new_coordinates == start:        #checks if the new position found is not our destination
            window.resetscreen()            #if it is then game is over
        if (new_coordinates in path):       #checks if the coordinates are in the path available to move
            turtle_current_y += 14.5
            turtle.goto(turtle_current_x, turtle_current_y)
            turtle.stamp()

    #creating a function to move our turtle backward in the y direction
    def backward():
        global turtle_current_y
        new_coordinates = (turtle_current_x, turtle_current_y - 14.5)
        if new_coordinates == start:
            window.resetscreen()
        if (new_coordinates in path):
            turtle_current_y -= 14.5
            turtle.goto(turtle_current_x, turtle_current_y)
            turtle.stamp()

    #creating a function to move our turtle left in the x direction
    def left():
        global turtle_current_x
        new_coordinates = (turtle_current_x - 14.5, turtle_current_y)
        if new_coordinates == start:
            window.resetscreen()
        if (new_coordinates in path):
            turtle_current_x -= 14.5
            turtle.goto(turtle_current_x, turtle_current_y)
            turtle.stamp()

    #creating a function to move our turtle right in the x direction
    def right():
        global turtle_current_x
        new_coordinates = (turtle_current_x + 14.5, turtle_current_y)
        if new_coordinates == start:
            window.resetscreen()
        if (new_coordinates in path):
            turtle_current_x += 14.5
            turtle.goto(turtle_current_x, turtle_current_y)
            turtle.stamp()

    # Turtle Properties
    t = turtle.Turtle()
    turtle.shapesize(0.67, 0.67, 0.67)
    turtle.penup()
    turtle.speed(0)
    turtle.setheading(90)

    # Starting position
    global turtle_current_x
    global turtle_current_y
    turtle_current_x = finish_x
    turtle_current_y = finish_y
    turtle.goto(turtle_current_x, turtle_current_y)

    #assigns all the functions we created to the respective arrow keys
    turtle.onkey(forward, 'Up')
    turtle.onkey(backward, 'Down')
    turtle.onkey(left, 'Left')
    turtle.onkey(right, 'Right')
    turtle.shape("square")
    turtle.color("#800000")
    turtle.listen()

    #exits the window when we click on it after the process ends
    window.exitonclick()


# calling our main function
level_2()
