import numpy as np # import numpy to create 2d arrays


class Plate:

    # initialize with given size and category
    def __init__(self, height, width, category):
        self.width = width
        self.height = height
        self.category = category
        self.state = np.zeros((height, width), dtype=np.int16) # create np array of given size with only zeros
        self.current_y = 0

    # if possible, add the given shelf to the plate and adjust current_y accordingly, else, return false
    def add_shelf(self, shelf):
        if not shelf.shelf_height + self.current_y > self.height:
            self.state[self.current_y:(self.current_y + shelf.shelf_height)] = shelf.state
            self.current_y += shelf.shelf_height
            return True
        else:
            return False


class Shelf:

    # initialize with given size and category
    def __init__(self, height, width, category):
        self.shelf_width = width
        self.shelf_height = height
        self.category = category
        self.state = np.zeros((height, width), dtype = np.int16) # create np array of given size with only zeros
        self.current_x = 0

    # if possible, add the given order to the shelf and adjust current_x accordingly, else, return false
    def add_order(self, order_height, order_width):
        if not order_width + self.current_x > self.shelf_width:
            self.state[(self.shelf_height - order_height):self.shelf_height, self.current_x:(order_width +
                                                                                             self.current_x)] = 1
            self.current_x += order_width
            return True
        else:
            return False

