from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import random

class Creature:
    def __init__(self, xpos, ypos, color):
        self.xpos = xpos
        self.ypos = ypos
        self.color = color

x = [1]
y = [random.randint(1,10)]

fig, ax = plt.subplots()
graph = ax.plot(x, y,color ='g')[0]
plt.ylim(0,10)

def update(frame):
    global graph

    x.append(random.randint(1, 10))

    graph.set_xdata(x)
    graph.set_ydata(y)
    plt.xlim(x[0], x[-1])

anim = FuncAnimation(fig, update, frames=None)
plt.show()
