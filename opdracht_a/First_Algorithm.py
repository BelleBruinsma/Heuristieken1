from classes import *  # import classes Shelf and Plate
from scipy.misc import toimage

# declare height and width of plate types
WIDTH_TYPE = {1: 50}
HEIGHT_TYPE = {1: 60}

# orders in a list [height, width, type], sorted by type > height > width
order_list = [[34, 18, 1], [33, 14, 1], [32, 10, 1], [30, 19, 1], [29, 12, 1], [29, 11, 1], [27, 19, 1], [27, 11, 1],
              [25, 17, 1], [22, 11, 1], [22, 7, 1], [20, 10, 1], [18, 17, 1], [17, 12, 1], [16, 12, 1], [16, 9, 1],
              [16, 9, 1], [13, 4, 1], [12, 9, 1], [10, 9, 1]]

# initialize the first plate and shelf to be used by the algorithm
plate_list = [Plate(HEIGHT_TYPE[1], WIDTH_TYPE[1], order_list[0][2])]
shelf_list = [Shelf(order_list[0][0], WIDTH_TYPE[1], order_list[0][2])]

# try to add every order to a shelf, if no available shelf is found, create new shelf with own height and type
for current_order in order_list:
    for current_shelf in shelf_list:
        if current_shelf.add_order(current_order[0], current_order[1]):
            break
        if current_shelf == shelf_list[-1]:
            shelf_type = current_order[2]
            shelf_list.append(Shelf(current_order[0], WIDTH_TYPE[shelf_type], shelf_type))

print("The following shelfs have been created: \n")

# print the created shelfs in terminal
for x in shelf_list:
    print("**********************\n")
    print(x.state)
    print("\n")

# try to add every shelf to a plate, if no available plate is found, create new plate with own height and type
for current_shelf in shelf_list:
    for current_plate in plate_list:
        if current_plate.add_shelf(current_shelf):
            break
        if current_plate == plate_list[-1]:
            plate_type = current_shelf.category
            plate_list.append(Plate(HEIGHT_TYPE[plate_type], WIDTH_TYPE[plate_type], plate_type))

print("\n This resulted in the following way of filling the plates:\n")

# print the created plates in terminal
for x in plate_list:
    print("**********************\n")
    print(x.state)
    print("\n")

toimage(plate_list[0].state).show()