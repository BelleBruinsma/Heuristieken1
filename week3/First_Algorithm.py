import numpy as np

WIDTH_TYPE_1 = 5
HEIGHT_TYPE_1 = 6


class Glasplaat:

    def __init__(self, height, width, category):
        self.width = width
        self.height = height
        self.category = category
        self.state = np.zeros((height, width), dtype = np.int16)
        self.current_y = 0

    def add_shelf(self, shelf):
        if not shelf.shelf_height + self.current_y > self.height:
            self.state[self.current_y:(self.current_y + shelf.shelf_height)] = shelf.state
            self.current_y += shelf.shelf_height
            return True
        else:
            return False


class Shelf:

    def __init__(self, height, width, category):
        self.shelf_width = width
        self.shelf_height = height
        self.category = category
        self.state = np.zeros((height, width), dtype = np.int16)
        self.current_x = 0

    def add_order(self, order_height, order_width):
        if not order_width + self.current_x > self.shelf_width:
            self.state[(self.shelf_height - order_height):self.shelf_height, self.current_x:(order_width + self.current_x)] = 1
            self.current_x += order_width
            return True
        else:
            return False

order_list = [[4, 3], [3, 2], [3, 2], [3, 2], [2, 2], [2, 1], [1, 2], [1, 1]]

plate_list = [Glasplaat(HEIGHT_TYPE_1, WIDTH_TYPE_1, 1)]
shelf_list = [Shelf(order_list[0][0], WIDTH_TYPE_1, 1)]

for current_order in order_list:
    for current_shelf in shelf_list:
        if current_shelf.add_order(current_order[0], current_order[1]):
            break
        if current_shelf == shelf_list[-1]:
            shelf_list.append(Shelf(current_order[0], WIDTH_TYPE_1, 1))

print("The following layers have been created: \n")

for x in shelf_list:
    print("**********************\n")
    print(x.state)
    print("\n")

for current_shelf in shelf_list:
    for current_plate in plate_list:
        if current_plate.add_shelf(current_shelf):
            break
        if current_plate == plate_list[-1]:
            plate_list.append(Glasplaat(HEIGHT_TYPE_1, WIDTH_TYPE_1, 1))

print("\n This resulted in the following way of filling the plates:\n")

for x in plate_list:
    print("**********************\n")
    print(x.state)
    print("\n")



