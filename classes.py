import numpy as np  # import numpy to create 2d arrays
np.set_printoptions(threshold=np.nan)

class Node:
    def __init__(self, id_, values, previous_area=0):
        self.id = id_
        self.total_area = previous_area + values[1]
        self.parent = []
        self.values = values[0]
        self.area = values[0][0] * values[0][1]
        self.children = []
        self.used = []
        self.used_areas = []

    def add_child(self, node):
        self.children.append(node)

    def get_children(self):
        return self.children

    def remove_child(self, child_id):
        self.children = [child for child in self.children if not child.id == child_id]

    def add_used_node(self, node):
        self.used.append(node)
        self.used_areas.append(node.area)


class Plate:

    # initialize with given size and category
    def __init__(self, height, width, category):
        self.width = width
        self.height = height
        self.category = category
        self.state = np.zeros((height, width), dtype=np.int16)  # create np array of given size with only zeros
        self.current_y = 0
        self.opt_cord = [[height, 0]]

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
        self.state = np.zeros((height, width), dtype=np.int16)  # create np array of given size with only zeros
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

