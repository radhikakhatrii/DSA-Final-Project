# import practice
from tkinter import *

root = Tk()


def on_click_level1():
    import main_project_file_level1
    execfile("main_project_file_level1.py")


def on_click_level2():
    import main_project_file_level2
    execfile("main_project_file_level2.py")


def on_click_level3():
    import main_project_file_level3
    execfile("main_project_file_level3.py")


def on_click_level4():
    import main_project_file_level4
    execfile("main_project_file_level4.py")


myButton = Button(root, text="Level 1", fg="white", bg="#914350",
                  font="Verdana 40", padx=200, pady=15, command=on_click_level1)
myButton2 = Button(root, text="Level 2", fg="#914350", bg="white",
                   font="Verdana 40", padx=200, pady=15, command=on_click_level2)
myButton3 = Button(root, text="Level 3", fg="white", bg="#914350",
                   font="Verdana 40", padx=200, pady=15, command=on_click_level3)
myButton4 = Button(root, text="Level 4", fg="#914350", bg="white",
                   font="Verdana 40", padx=200, pady=15, command=on_click_level4)
myLabel = Label(root, text='')

myLabel.grid(row=0, column=0)
myButton.grid(row=2, column=1)
myButton2.grid(row=6, column=1)
myButton3.grid(row=10, column=1)
myButton4.grid(row=14, column=1)

root.mainloop()
