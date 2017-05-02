import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
ax.set_xlim(0,60)
ax.set_ylim(0,50)
for p in [
    patches.Rectangle(
        (0,0), 34, 18, fc='red'
    ),
    patches.Rectangle(
        (0,18), 33, 14, fc='green'
    ),
    patches.Rectangle(
        (34, 0), 10, 32, fc='pink'
    ),
    patches.Rectangle(
        (0, 32), 30, 19, fc='yellow'
    ),
    patches.Rectangle(
        (44, 0), 4, 24, fc='brown'
    ),
    patches.Rectangle(
        (30, 32), 20, 10, fc='orange'
    ),
    patches.Rectangle(
        (30, 42), 18, 17,
    ),
]:
    ax.add_patch(p)

plt.show()


#plt.axis([0, 60, 0, 50])
#plt.ylabel('meters')
#plt.axvspan(5, 10, 0, 0.2, facecolor='g', alpha=0.5) #alpha is the transparency

#order1 = plt.figure()

#patches.Rectangle((0,0), 34, 180, fc='g')
#plt.show()

