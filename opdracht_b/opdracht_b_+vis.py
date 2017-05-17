from rectpack import newPacker #guillo #sky
import matplotlib.pyplot as plt
import matplotlib.patches as patches


rectangles = [(150, 150), (50, 110), (160, 270), (130, 270), (130, 130), (190, 160), (200, 190), (170, 240), \
(110, 220), (110, 140), (70, 230), (140, 170), (160, 240), (200, 130), (150, 100), (190, 220), (60, 150), (40, 240), \

# order 3
(110, 100), (130, 240), (130, 220), (90, 160), (40, 100), (50, 140), (150, 250), (70, 200), (160, 120), (120, 120), \
(100, 190), (190, 240), (120, 270), (60, 130), (160, 230), (170, 170), (200, 170), (90, 210), (60, 190), \
(120, 180), (110, 190), (180, 270), (160, 120), (160, 100), \

#order 4
(90, 220), (110, 260), (80, 120), (80, 280), (50, 280), (80, 270), (160, 190), (40, 190), (90, 250), (180, 210), \
(180, 250), (110, 160), (170, 270), (110, 270), (80, 140), (100, 270), (140, 210), (120, 200), (120, 150)]

bins = [(600, 500), (600,500), (600,500), (600, 500), (600, 500), (600,500), (600,500), (600, 500)]

packer = newPacker()

# Add the rectangles to packing queue
for r in rectangles:
	packer.add_rect(*r)

# Add the bins where the rectangles will be placed
for b in bins:
	packer.add_bin(*b)

# Start packing
packer.pack()

# Obtain number of bins used for packing
nbins = len(packer)

# Index first bin
abin = packer[0]

# Bin dimmensions (bins can be reordered during packing)
width, height = abin.width, abin.height

# Print: bin, x, y,
print(packer.rect_list())
pos = packer.rect_list()

# Number of rectangles packed into every bin
nrect0 = len(packer[0])
nrect1 = len(packer[1])
nrect2 = len(packer[2])

print("The first bin takes %d orders" %(nrect0))
print("The second bin takes %d orders" %(nrect1))
print("The third bin takes %d orders" %(nrect2))
print("The total number of bins that is used is %d" %(nbins))

# draw right amount of figures
for i in range(nbins):
    fig = plt.figure()
    ax= fig.add_subplot(111, aspect='equal')
    ax.set_xlim(0, 600)
    ax.set_ylim(0, 500)

# draw rectangles
for i in pos:
    xas = i[1]
    yas = i[2]
    width = i[3]
    height = i[4]
    if i[0] == 0:
        ax.add_patch(
            patches.Rectangle(
                (xas,yas),
                width,
                height,
            )
        )
    elif i[0] == 1:
        fig2 = plt.figure(2)
        ax2 = fig2.add_subplot(111, aspect='equal')
        ax2.set_xlim(0, 600)
        ax2.set_ylim(0, 500)
        ax2.add_patch(
            patches.Rectangle(
                (xas, yas),
                width,
                height,
            )
        )
    elif i[0] == 2:
        fig3 = plt.figure(3)
        ax1 = fig3.add_subplot(111, aspect='equal')
        ax1.set_xlim(0, 600)
        ax1.set_ylim(0, 500)
        ax1.add_patch(
            patches.Rectangle(
                (xas, yas),
                width,
                height,
            )
        )
    elif i[0] == 3:
        fig4 = plt.figure(4)
        ax1 = fig4.add_subplot(111, aspect='equal')
        ax1.set_xlim(0, 600)
        ax1.set_ylim(0, 500)
        ax1.add_patch(
            patches.Rectangle(
                (xas, yas),
                width,
                height,
            )
        )
    elif i[0] == 4:
        fig5 = plt.figure(5)
        ax1 = fig5.add_subplot(111, aspect='equal')
        ax1.set_xlim(0, 600)
        ax1.set_ylim(0, 500)
        ax1.add_patch(
            patches.Rectangle(
                (xas, yas),
                width,
                height,
            )
        )
    else:
        fig1 = plt.figure(1)
        ax1 = fig1.add_subplot(111, aspect='equal')
        ax1.set_xlim(0, 600)
        ax1.set_ylim(0, 500)
        ax1.add_patch(
            patches.Rectangle(
                (xas, yas),
                width,
                height,
            )
        )

plt.show()