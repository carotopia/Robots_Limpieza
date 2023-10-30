import tkinter as tk
import time
import random

class CleaningRobot:
    def __init__(self, canvas, color, x, y):
        self.canvas = canvas
        self.color = color
        self.x = x
        self.y = y
        self.cleaned_points = set()

    def clean(self):
        self.canvas.create_oval(self.x, self.y, self.x + 10, self.y + 10, fill=self.color)
        self.cleaned_points.add((self.x, self.y))

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy


        if (0 <= new_x < 400) and (0 <= new_y < 400):

            if (new_x, new_y) not in self.cleaned_points:
                self.x = new_x
                self.y = new_y

window = tk.Tk()
window.title("Cleaning Robots")
canvas = tk.Canvas(window, width=200, height=200)
canvas.pack()

for x in range(0, 400, 10):
    for y in range(0, 400, 10):
        canvas.create_oval(x, y, x + 10, y + 10, fill="black")

robot1 = CleaningRobot(canvas, "red", 0, 0)
robot2 = CleaningRobot(canvas, "blue", 10, 0)

def clean_grid_random():
    for _ in range(400):
        dx1, dy1 = random.choice([(10, 0), (-10, 0), (0, 10), (0, -10)])
        dx2, dy2 = random.choice([(10, 0), (-10, 0), (0, 10), (0, -10)])

        robot1.move(dx1, dy1)
        robot2.move(dx2, dy2)

        if (robot1.x, robot1.y) not in robot1.cleaned_points:
            robot1.clean()

        if (robot2.x, robot2.y) not in robot2.cleaned_points:
            robot2.clean()

        window.update()
        time.sleep(0.1)

clean_grid_random()

window.mainloop()
