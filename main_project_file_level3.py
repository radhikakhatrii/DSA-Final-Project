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


def level_3():
    # A dictionary to keep a record of visited pixels when running BFS on our maze
    pixels_visited = {}
    path = []  # list of nodes to be visited during BFS search
    queue = []  # this list keeps the record of next node to be visited
    visited = []  # keeps record of the visited nodes so that they should not be visited again
    # defining the main turtle screen using turtle library
    window = turtle.Screen()
    window.delay(0)  # a helpful function for faster execution
    # the background of main window is defined as black
    window.bgcolor("white")
    window.title("Level 3")  # tentative window name
    window.setup(1050, 620)  # window dimensions to suit the size of maze

    # this function creates the walls of the maze and assigns the pixels of the paths that can be visited by the player
    def create_maze_level_3(frame):
        global begin_x, begin_y, finish_x, finish_y
        # defining a turtle's specifications to create the walls of our maze
        maze = turtle.Turtle()
        maze.shape('square')
        maze.color("#ff0066")
        # the size helps us to fit the maze within the window frame
        maze.shapesize(0.67, 0.67, 0.67)
        maze.penup()  # this hides the working of turtle in background from the user
        maze.speed(0)  # hides the moving turtle across the screen
        # iterating over the rows and columns of our frame to visit each and every character
        for y in range(len(frame)):
            for x in range(len(frame[y])):
                character = frame[y][x]
                # these variables defines the pixel on the screen where the program will start drawing its maze from
                screen_x = -502 + (x * 13)
                screen_y = 291 - (y * 13)
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
        tracker.color('#ff4da6')
        tracker.penup()  # hides the working of turtle in background from the user
        tracker.speed(0)  # hides the moving turtle across the screen
        # the size helps us to fit the maze within the window frame
        tracker.shapesize(0.67, 0.67, 0.67)
        while len(queue) > 0:  # while queue is not empty
            time.sleep(0)  # executes the next line of code
            x, y = queue.pop(0)  # the first element from queue is popped
            if(x - 13, y) in path and (x - 13, y) not in visited:  # check the cell left
                cell = (x - 13, y)  # coordinate for the cell left
                pixels_visited[cell] = x, y
                queue.append(cell)   # adds cell to queue list
                visited.append((x-13, y))  # adds cell to visited list
            if (x, y - 13) in path and (x, y - 13) not in visited:  # check the cell down
                cell = (x, y - 13)  # coordinate for the cell down
                pixels_visited[cell] = x, y
                queue.append(cell)  # adds cell to queue list
                visited.append((x, y - 13))  # adds cell to visited list
                # print(pixels_visited)
            if (x + 13, y) in path and (x + 13, y) not in visited:   # check the cell right
                cell = (x + 13, y)  # coordinate for the cell right
                pixels_visited[cell] = x, y
                queue.append(cell)  # adds cell to queue list
                visited.append((x + 13, y))  # adds cell to visited list
            if (x, y + 13) in path and (x, y + 13) not in visited:  # check the cell up
                cell = (x, y + 13)  # coordinate for the cell up
                pixels_visited[cell] = x, y
                queue.append(cell)  # adds cell to queue list
                visited.append((x, y + 13))  # adds cell to visited list
            tracker.goto(x, y)
            tracker.stamp()

    def back_tracking(x, y):
        back_track = turtle.Turtle()
        back_track.shape('square')
        back_track.color('#ff80ff')
        back_track.penup()
        back_track.speed(0)
        back_track.shapesize(0.67, 0.67, 0.67)
        back_track.goto(x, y)
        back_track.stamp()
        # the method below has a pre-requisite of running the BFS function first where we search for all pixels that can be visited in the pixels_visited dictionary
        # while (x, y) != (begin_x, begin_y):
        #     back_track.goto(pixels_visited[x, y])
        #     back_track.stamp()
        #     x, y = pixels_visited[x, y]
        # we instead use this alternate method where we ony run BFS once and calculate all the pixels that are there in the shortest path so that when timer gets over, the user doesnt have to wait a long time of waiting for BFS to look what the shortest path was
        # final_path=[]
        # while (x, y) != (begin_x, begin_y):
        #    x, y = pixels_visited[x, y]
        #    final_path.append((x,y))
        # print(final_path)
        # using the solution above we print the final path in the terminal and then copy the solution into a final_path variable
        final_path = [(460, -281), (447, -281), (434, -281), (421, -281), (421, -268), (421, -255), (421, -242), (408, -242), (395, -242), (395, -229), (395, -216), (395, -203), (395, -190), (395, -177), (395, -164), (395, -151), (408, -151), (421, -151), (421, -138), (421, -125), (408, -125), (395, -125), (395, -112), (395, -99), (395, -86), (395, -73), (395, -60), (395,
                                                                                                                                                                                                                                                                                                                                                                                  -47), (395, -34), (408, -34), (421, -34), (421, -21), (421, -8), (408, -8), (395, -8), (382, -8), (369, -8), (356, -8), (356, 5), (356, 18), (356, 31), (356, 44), (356, 57), (356, 70), (343, 70), (330, 70), (317, 70), (304, 70), (291, 70), (278, 70), (265, 70), (252, 70), (239, 70), (226, 70), (226, 83), (226, 96), (226, 109), (226, 122), (226, 135), (226, 148), (226, 161), (226, 174), (226, 187), (226, 200), (226, 213), (226, 226), (213, 226), (200, 226), (200, 213), (200, 200), (200, 187), (187, 187), (174, 187), (161, 187), (148, 187), (135, 187), (135, 174), (135, 161), (135, 148), (135, 135), (135, 122), (135, 109), (122, 109), (109, 109), (96, 109), (83, 109), (70, 109), (70, 96), (70, 83), (70, 70), (57, 70), (44, 70), (31, 70), (18, 70), (5, 70), (5, 57), (5, 44), (-8, 44), (-21, 44), (-34, 44), (-47, 44), (-60, 44), (-73, 44), (-86, 44), (-99, 44), (-99, 57), (-99, 70), (-112, 70), (-125, 70), (-138, 70), (-151, 70), (-164, 70), (-177, 70), (-190, 70), (-203, 70), (-216, 70), (-229, 70), (-242, 70), (-255, 70), (-268, 70), (-281, 70), (-294, 70), (-294, 83), (-294, 96), (-294, 109), (-294, 122), (-294, 135), (-294, 148), (-294, 161), (-294, 174), (-294, 187), (-307, 187), (-320, 187), (-333, 187), (-346, 187),
                      (-359, 187), (-372, 187), (-385, 187), (-398, 187), (-411, 187), (-424, 187), (-437, 187), (-450, 187), (-463, 187), (-476, 187), (-489, 187), (-489, 200), (-489, 213), (-489, 226), (-489, 239), (-489, 252), (-489, 265), (-489, 278), (-502, 278)]
        for i in final_path:
            back_track.goto(i)
            back_track.stamp()

    frame = [
        "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++",
        "s    +         +                        +                                  +",
        "+    +         +                        +                                  +",
        "+    +    +    +    +    +++++++++++    +    ++++++++++++++++    +    ++++++",
        "+    +    +         +         +         +         +         +    +         +",
        "+    +    +         +         +         +         +         +    +         +",
        "+    +++++++++++++++++++++    +++++++++++    ++++++    +    +    ++++++    +",
        "+                   +         +              +         +    +    +         +",
        "+                   +         +              +         +    +    +         +",
        "++++++++++++++++    +    +    +    +++++++++++    ++++++    +    +    ++++++",
        "+              +    +    +    +    +         +    +    +    +    +         +",
        "+              +    +    +    +    +         +    +    +    +    +         +",
        "+    ++++++    +    +    ++++++    +    ++++++    +    +    +    ++++++    +",
        "+         +    +    +                   +         +    +    +         +    +",
        "+         +    +    +                   +         +    +    +         +    +",
        "++++++    +    +    +++++++++++++++++++++    ++++++    +    +++++++++++    +",
        "+         +    +                   +         +         +              +    +",
        "+         +    +                   +         +         +              +    +",
        "+    ++++++    ++++++++++++++++    +    ++++++    ++++++++++++++++    +    +",
        "+    +                        +         +                        +    +    +",
        "+    +                        +         +                        +    +    +",
        "++++++    +    ++++++++++++++++++++++++++++++++++++++++++++++    +    +    +",
        "+         +    +                                       +         +         +",
        "+         +    +                                       +         +         +",
        "+    ++++++    +    +++++++++++    ++++++++++++++++    +    +    ++++++    +",
        "+    +         +    +    +         +              +         +    +         +",
        "+    +         +    +    +         +              +         +    +         +",
        "+    ++++++    +    +    +    +++++++++++    +    +++++++++++    +    ++++++",
        "+         +    +         +    +              +              +    +    +    +",
        "+         +    +         +    +              +              +    +    +    +",
        "+    +    ++++++    ++++++    +    ++++++++++++++++++++++++++    +    +    +",
        "+    +              +         +         +                   +    +         +",
        "+    +              +         +         +                   +    +         +",
        "+    ++++++++++++++++    +++++++++++    +    +++++++++++    +    ++++++    +",
        "+              +    +    +              +    +         +         +         +",
        "+              +    +    +              +    +         +         +         +",
        "+++++++++++    +    +    ++++++    ++++++    +    +    +++++++++++    ++++++",
        "+    +              +         +                   +              +    +    +",
        "+    +              +         +                   +              +    +    +",
        "+    +    ++++++++++++++++    +    ++++++++++++++++++++++++++    +    +    +",
        "+         +                   +              +              +    +         +",
        "+         +                   +              +              +    +         +",
        "+    ++++++    +++++++++++++++++++++++++++++++    ++++++    +++++++++++    +",
        "+         +                                            +                   +",
        "+         +                                            +                   e",
        "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
    ]
    # we use this function to find the coordinates of the screen to start creating the maze from those coordinates so that it fits the screen size
    # def buttonclick(x,y):
    #     print("You clicked at this coordinate({0},{1})".format(x,y))

    # #onscreen function to send coordinate
    # turtle.onscreenclick(buttonclick,1)
    # turtle.listen()  # listen to incoming connections
    # turtle.speed(10) # set the speed
    # turtle.done()    # hold the screen

    # calling all the functions within our main function
    create_maze_level_3(frame)
    # we comment out the BFS function once we have completed all steps to generate the final path
    # Breadth_First_Search(begin_x, begin_y)
    import threading

    def timer():        # timer fucntion
        window.title('GAME OVERR!!')
        back_tracking(finish_x, finish_y)

    delay = 90  # calls backtracking function after 1 and a half minute
    start_time = threading.Timer(delay, timer)
    start_time.start()
    # back_tracking(finish_x, finish_y)

    # now we will create functions for our player to move the turtle
    # this records the coordinates of our destination point on screen
    start = (begin_x, begin_y)
    # creating a function to move our turtle forward in the y direction

    def forward():
        # var to keep track of the coordinate where our turtle currently is
        global turtle_current_y
        new_coordinates = (turtle_current_x, turtle_current_y + 13)
        if new_coordinates == start:  # checks if the new position found is not our destination
            window.resetscreen()  # if it is then game is over
        if (new_coordinates in path):  # checks if the coordinates are in the path available to move
            turtle_current_y += 13
            turtle.goto(turtle_current_x, turtle_current_y)
            turtle.stamp()

    # creating a function to move our turtle backward in the y direction
    def backward():
        global turtle_current_y
        new_coordinates = (turtle_current_x, turtle_current_y - 13)
        if new_coordinates == start:
            window.resetscreen()
        if (new_coordinates in path):
            turtle_current_y -= 13
            turtle.goto(turtle_current_x, turtle_current_y)
            turtle.stamp()

    # creating a function to move our turtle left in the x direction
    def left():
        global turtle_current_x
        new_coordinates = (turtle_current_x - 13, turtle_current_y)
        if new_coordinates == start:
            window.resetscreen()
        if (new_coordinates in path):
            turtle_current_x -= 13
            turtle.goto(turtle_current_x, turtle_current_y)
            turtle.stamp()

    # creating a function to move our turtle right in the x direction
    def right():
        global turtle_current_x
        new_coordinates = (turtle_current_x + 13, turtle_current_y)
        if new_coordinates == start:
            window.resetscreen()
        if (new_coordinates in path):
            turtle_current_x += 13
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

    # assigns all the functions we created to the respective arrow keys
    turtle.onkey(forward, 'Up')
    turtle.onkey(backward, 'Down')
    turtle.onkey(left, 'Left')
    turtle.onkey(right, 'Right')
    turtle.shape("square")
    turtle.color("#800000")
    turtle.listen()

    # exits the window when we click on it after the process ends
    window.exitonclick()


# calling our main function
level_3()
