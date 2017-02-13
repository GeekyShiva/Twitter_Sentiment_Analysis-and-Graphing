import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

style.use("ggplot")

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)


def animate(i):
    pullData = open("twitter-out.txt", "r").read()   ## data-file name , put name where datafile is stored
    lines = pullData.split('\n')

    xar = []
    yar = []

    x = 0
    y = 0

    for l in lines[-200:]:          ## this saves the last 200 lines of data to put on for graphing.
        x += 1
        if "pos" in l:
            y += 1
        elif "neg" in l:
            y -= 1                    ## to remove the negative graphing you can put 0.3 instead 1

        xar.append(x)
        yar.append(y)

    ax1.clear()
    ax1.plot(xar, yar)


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()