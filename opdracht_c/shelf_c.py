from classes_c import *
import time
from sort_c import *
from functions_c import *
import numpy

start_time = time.time()

# declare height and width of plate types
PLATE_SIZE = {1: {'height': 60, 'width': 50}, 2: {'height': 50, 'width': 40}, 3: {'height': 40, 'width': 40}}

# orders in a list [height, width]
order_list_1 = [[13, 24], [17, 19], [15, 15], [7, 16], [16, 21], [11, 14], [11, 17], [15, 17], [15, 23], [6, 12],
                [16, 15], [16, 24], [7, 16], [12, 23], [14, 12], [13, 24], [9, 18], [15, 23], [10, 15], [8, 18], [13, 18]]

order_list_2 = [[15, 21], [15, 15], [10, 23], [11, 11], [7, 24], [15, 23], [17, 22], [15, 19], [18, 21], [13, 12],
                [17, 23], [9, 20], [15, 23], [14, 19], [12, 13], [16, 15], [11, 10], [8, 19], [8, 23], [7, 18], [7,11]]

order_list_3 = [[18, 10], [9, 13], [7, 18], [15, 12], [6, 20], [8, 20], [6, 24], [11, 16], [12, 24], [11, 17], [15, 23]]

# order lists
order_list = {1: order_list_1, 2: order_list_2, 3: order_list_3}
#------------------------------------------------
# TYPE 3
#------------------------------------------------

# sort order_list_3 by height
order_list[3] = sort_height(order_list[3])

# initialize the first plate and shelf to be used by the algorithm of type 3
plate_list_3 = [Plate(height = PLATE_SIZE[3]['height'], width =  PLATE_SIZE[3]['width'], category =  3)]

# shelf has height equal to the height of the first element of the order list (order_list[3][0][0])
shelf_list_3 = [Shelf(height = order_list[3][0][0], width = PLATE_SIZE[3]['width'], category = 3)]

# try to add every order to a shelf, if no available shelf is found, create new shelf with own height and type
for current_order in order_list[3]:
    for current_shelf in shelf_list_3:
        if current_shelf.add_order(order_height = current_order[0], order_width = current_order[1]):
            break
        if current_shelf == shelf_list_3[-1]:
            shelf_list_3.append(Shelf(height = current_order[0], width = PLATE_SIZE[3]['width'], category = 3))

# try to add every shelf to a plate, if no available plate is found, create new plate with own height and type
for current_shelf in shelf_list_3:
     for current_plate in plate_list_3:
         if current_plate.add_shelf(current_shelf):
             break
         if current_plate == plate_list_3[-1]:
             plate_type = current_shelf.category
             plate_list_3.append(Plate(PLATE_SIZE[3]['height'], PLATE_SIZE[3]['width'], 3))

# show plates in csv file
for i in range(0,len(plate_list_3)):
    numpy.savetxt("old_plate_3_"+str(i)+".csv", plate_list_3[i].state, delimiter="", fmt='%1.0f')

#------------------------------------------------
# check if we can fit a type 2 order in the waste of type 3

# list_3 = [plate_list_3[0].state, plate_list_3[1].state]
list_3 = map(lambda x: x.state, plate_list_3)

order_list_2_clean = []

for z in range(len(order_list_2)):
    # get the largest rectangle from all plates of type 3
    list_3_area_max = map(lambda x: getMaxArea(x), list_3)

    # get the size of the largest rectangles
    list_3_area_height_width = map(lambda x: getCoordinates(x), list_3_area_max)

    list_3_area_size = map(lambda x: x[0] * x[1], list_3_area_height_width)

    # initialize lists for in loop
    if order_list_2_clean == []:
        loop_list = order_list_2
    else:
        loop_list = order_list_2_clean

    # list with the orders of order_list_2 that fits in the rectangle waste
    list_2_waste_3_orders = []

    # loop over list_3_area_height_width and iteratively delete orders from order_list_2 (loop_list)
    for i in range(0,len(list_3_area_height_width)):
        function_result = getCleanOrderList(area_size = list_3_area_height_width[i], orderlist = loop_list)
        loop_list = function_result[0]

        #print("Loop list die over is", loop_list)

        if not len(function_result[1]) == 0:
            list_2_waste_3_orders.append(function_result[1])

    # assign new (clean) order_list_2
    if order_list_2_clean == loop_list:
        break

    order_list_2_clean = loop_list

    # create new order plates
    newPlate(list = list_3, waste_order = list_2_waste_3_orders, area_max = list_3_area_max, category = 3)

#------------------------------------------------
# TYPE 2
#------------------------------------------------

#sort clean order list 2 by height
order_list_2_clean = sort_height(order_list_2_clean)

# initialize the first plate and shelf to be used by the algorithm of type 2
plate_list_2 = [Plate(height = PLATE_SIZE[2]['height'], width =  PLATE_SIZE[2]['width'], category =  2)]

# shelf has height equal to the height of the first element of the order_list_2_clean (the one who is cleaned up by type 3)
shelf_list_2 = [Shelf(height = order_list_2_clean[0][0], width = PLATE_SIZE[2]['width'], category = 2)]

# try to add every order to a shelf, if no available shelf is found, create new shelf with own height and type
for current_order in order_list_2_clean:
    for current_shelf in shelf_list_2:
        if current_shelf.add_order(order_height = current_order[0], order_width = current_order[1]):
            break
        if current_shelf == shelf_list_2[-1]:
            shelf_list_2.append(Shelf(height = current_order[0], width = PLATE_SIZE[2]['width'], category = 2))

# try to add every shelf to a plate, if no available plate is found, create new plate with own height and type
for current_shelf in shelf_list_2:
     for current_plate in plate_list_2:
         if current_plate.add_shelf(current_shelf):
             break
         if current_plate == plate_list_2[-1]:
             plate_type = current_shelf.category
             plate_list_2.append(Plate(PLATE_SIZE[2]['height'], PLATE_SIZE[2]['width'], 2))

# show plates in csv file
for i in range(0,len(plate_list_2)):
     numpy.savetxt("old_plate_2_"+str(i)+".csv", plate_list_2[i].state, delimiter="", fmt='%1.0f')

# ------------------------------------------------
# check if we can fit a type 2 order in the waste of type 3

# list_2 = [plate_list_2[0].state, plate_list_2[1].state]
list_2 = map(lambda x: x.state, plate_list_2)

order_list_1_clean = []

for z in range(len(order_list_1)):

    # get the largest rectangle from all plates of type 2
    list_2_area_max = map(lambda x: getMaxArea(x), list_2)

    # get the size of the largest rectangles
    list_2_area_height_width = map(lambda x: getCoordinates(x), list_2_area_max)

    # get the size of the area [height * width]
    list_2_area_size = map(lambda x: x[0] * x[1], list_2_area_height_width)

    # initialize lists for in loop
    if order_list_1_clean == []:
        loop_list_1 = order_list_1
    else:
        loop_list_1 = order_list_1_clean

    list_1_waste_2_orders = []

    # loop over list_2_area_height_width and iteratively delete orders from order_list_1 (loop_list)
    for i in range(0,len(list_2_area_height_width)):
        function_result = getCleanOrderList(area_size = list_2_area_height_width[i], orderlist = loop_list_1)

        loop_list_1 = function_result[0]

        if not len(function_result[1]) == 0:
            list_1_waste_2_orders.append(function_result[1])

    # assign new (clean) order_list_1
    if order_list_1_clean == loop_list:
        break
    order_list_1_clean = loop_list

    # create new order plates
    #newPlate(list=list_2, waste_order = list_1_waste_2_orders, area_max = list_2_area_max, category = 2)

# #------------------------------------------------
# # TYPE 1
# #------------------------------------------------

# sort clean order list 1 by height
order_list_1_clean = sort_height(order_list_1_clean)

# initialize the first plate and shelf to be used by the algorithm of type 1
plate_list_1 = [Plate(height = PLATE_SIZE[1]['height'], width =  PLATE_SIZE[1]['width'], category =  1)]

# shelf has height equal to the height of the first element of the order list (order_list[1][0][0])
shelf_list_1 = [Shelf(height = order_list_1_clean[0][0], width = PLATE_SIZE[1]['width'], category = 1)]

# try to add every order to a shelf, if no available shelf is found, create new shelf with own height and type
for current_order in order_list_1_clean:
    for current_shelf in shelf_list_1:
        if current_shelf.add_order(order_height = current_order[0], order_width = current_order[1]):
            break
        if current_shelf == shelf_list_1[-1]:
            shelf_list_1.append(Shelf(height = current_order[0], width = PLATE_SIZE[1]['width'], category = 1))

# try to add every shelf to a plate, if no available plate is found, create new plate with own height and type
for current_shelf in shelf_list_1:
     for current_plate in plate_list_1:
         if current_plate.add_shelf(current_shelf):
             break
         if current_plate == plate_list_1[-1]:
             plate_type = current_shelf.category
             plate_list_1.append(Plate(PLATE_SIZE[1]['height'], PLATE_SIZE[1]['width'], 1))

for i in range(0,len(plate_list_1)):
     numpy.savetxt("old_plate_1_"+str(i)+".csv", plate_list_1[i].state, delimiter="", fmt='%1.0f')














