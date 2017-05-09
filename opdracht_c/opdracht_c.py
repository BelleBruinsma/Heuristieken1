# TYPE I: standaard dubbel glas 5 x 6     --> type I & type II
# TYPE II: veiligheidsglas 4 x 5          --> type II & type III
# TYPE III: dubbel veiligheidsglas 4 x 4  --> alleen type III

from rectpack import newPacker

rectangles_type1 = [(130, 240), (170, 190), (150, 150), (70, 160), (160, 210), (110, 140), \
(110, 170), (150, 170), (150, 230), (60, 120), (160, 150), (160, 240), \
(70, 160), (120, 230), (140, 120), (130, 240), (90, 180), (150, 230), \
(100, 150), (80, 180), (130, 180)]


rectangles_type2 = [(150, 210), (150, 150), (100, 230), \
(110, 110), (70, 240), (150, 230), (170, 220), (150, 190), (180, 210), \
(130, 120), (170, 230), (90, 200), (150, 230), (140, 190), (120, 130), \
(160, 150), (110, 100), (80, 190), (80, 230), (70, 180)]


rectangles_type3 = [(180, 100), (90, 130), (70, 180), (150, 120), (60, 200), (80, 200), (60, 240), \
(110, 160), (120, 240), (110, 170), (150, 230)]

bins_type1 = [(500, 600), (500,600), (500,600), (500, 600)]
bins_type2 = [(500, 400), (500,400), (500,400), (500, 400)]
bins_type3 = [(400, 400), (400,400)]

packer = newPacker()

# Add the rectangles to packing queue
for r in rectangles_type3:
	packer.add_rect(*r)

# Add the rectangles to packing queue
#for a in rectangles_type2:
#	packer.add_rect(*a)

# Add the bins where the rectangles will be placed
for b in bins_type3:
	packer.add_bin(*b)

# Start packing
packer.pack()

# Obtain number of bins used for packing
nbins = len(packer)


while nbins == 2:
	for r in rectangles_type2:
		packer.add_rect(*r)

# Index first bin
abin = packer[0]

# Bin dimmensions (bins can be reordered during packing)
width, height = abin.width, abin.height

# Print: bin, x, y,
print(packer.rect_list())

# Number of rectangles packed into every bin
nrect0 = len(packer[0])
nrect1 = len(packer[1])
nrect2 = len(packer[2])
nrect3 = len(packer[3])

print("The first bin takes %d orders" %(nrect0))
print("The second bin takes %d orders" %(nrect1))
print("The first bin takes %d orders" %(nrect2))
print("The second bin takes %d orders" %(nrect3))
print("The total number of bins that is used is %d" %(nbins))

