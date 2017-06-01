from rectpack import newPacker
import matplotlib.pyplot as plt
import matplotlib.patches as patches

rectangles = [(190, 270), (90, 160), (120, 290), (110, 220), (160, 120), (90, 120), (200, 100), \
(110, 290), (120, 170), (100, 320), (90, 160), (190, 300), (170, 250), (180, 340), (170, 180), (90, 100), (110, 270), (70, 220), (40, 130), (140, 330), (130, 110), (40, 240)]

bins = [(500, 600), (500,600), (500,600), (500, 600)]

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
		edgecolor="black"
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
		edgecolor="black"
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
		edgecolor="black"
            )
        )


plt.show()
