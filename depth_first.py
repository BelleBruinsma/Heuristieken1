
import sys
from combination_check import *
sys.setrecursionlimit(100000)

# initialize global variables
area_list = []
start_id = 0
final_item_list = []
threshold = 2710
min_percentage = 95
min_value = (threshold/100) * min_percentage
final_total_areas = []

# order_list = [[150, 150], [50, 110], [160, 270], [130, 270], [130, 130], [190, 160], [200, 190], [170, 240],
# [110, 220], [110, 140], [70, 230], [140, 170], [160, 240], [200, 130], [150, 100], [190, 220], [60, 150], [40, 240]]

order_list = [[34, 18, 1], [33, 14, 1], [32, 10, 1], [30, 19, 1], [29, 12, 1], [29, 11, 1], [27, 19, 1], [27, 11, 1],
              [25, 17, 1], [22, 11, 1], [22, 7, 1], [20, 10, 1], [18, 17, 1], [17, 12, 1], [16, 12, 1], [16, 9, 1],
              [16, 9, 1], [13, 4, 1], [12, 9, 1], [10, 9, 1]]

# order_list = [[1, 10], [4, 50], [2, 50], [1, 50], [3, 50], [1, 25], [5, 50]]

# calculate and add area to order list
stack = [[w, w[0] * w[1]] for w in order_list]
areas = [order[1] for order in stack]
total_area_to_fill = sum(areas)

print(total_area_to_fill)


# key generator based in height for sorting
def get_key(item):
    return item[1]

# sort the order list by height
stack = sorted(stack, key=get_key, reverse=True)
print(stack)

# create starting node and add itself to used nodes
start = Node(start_id, stack.pop(0))
start.add_used_node(start)


# recursive function that searches for combination of areas where no more rectangle can be added without exceeding
# the area of the used bins
def find_combination(current, orders, node_id, checked="n"):
    # will be run at the first iteration of the function
    if not checked == "y":
        print("orders:")
        print(orders)
        # adds remaining orders as children to starting node
        for order_nr in range(len(orders)):
            current.add_child(Node(node_id, orders[order_nr]))
            node_id += 1
            # adds starting node as used node to created children
            current.children[order_nr].add_used_node(current)
            for used_nodes in current.used:
                current.children[order_nr].add_used_node(used_nodes)
            # adds previously added children as used node to created children, to prevent duplicate results
            if not order_nr == 0:
                for y in range(order_nr):
                    current.children[order_nr].add_used_node(current.children[y])
            node_id += 1

    # if current node has no more children to check, backtrack to parent and remove checked node as child
    elif current.parent and not current.children:
            temp_id = current.id
            current = current.parent
            current.remove_child(temp_id)
            return find_combination(current, orders, current.id, "y")

    # if fully backtracked to starting node with no more children to check, no feasible combo was found
    elif not current.parent and not current.children:
            print("No combo was found")
            print(final_total_areas)
            return False

    # iterate over children to find possible addition of rectangle without exceeding maximum area
    for child in current.children:
        if child.area + current.total_area < threshold:
            added_children = 0
            child.total_area += current.total_area  # add area of child to total area
            child.add_used_node(current)
            # add used nodes of current node to child to prevent duplicates
            for used in current.used:
                child.add_used_node(used)
            # add orders that were not yet used nodes to children of found node
            for order in range(len(orders)):
                if not orders[order][1] in child.used_areas and not orders[order][1] == child.area:
                    child.add_child(Node(node_id, orders[order]))
                    # if children were added, assign already added children to used nodes
                    if added_children > 0:
                        for g in range(added_children):
                            child.children[added_children].add_used_node(child.children[g])
                    added_children += 1
                    node_id += 1
            # assign current node as parent for child for possible backtracking
            child.parent = current
            # child is new current node and function is called again
            current = child
            return find_combination(current, orders, node_id, "y")

        # if currently checked child is last in list of children > no more addition of rectangles is possible
        elif child == current.children[-1]:
            # append total area found to list for later debugging
            final_total_areas.append(current.total_area)
            child.parent = current.parent
            values = []
            while child.parent:
                values.append(child.values)
                child = child.parent
            values.append(child.values)
            attempt_list = make_list(values)
            for attempt in attempt_list:
                test_plate = Plate(60, 50, 1)
                h = try_combo(attempt, test_plate)
                if h:
                    total = 0
                    for cur in attempt:
                        total += cur[0]*cur[1]
                    if total >= min_value:
                        print()
                        print(test_plate.state)
                        print total
                        return True, h[1]
            # if combination didn't work, backtrack and remove last checked node from children
            print("onto the next one")
            temp_id = current.id
            current.parent.add_used_node(current)
            current = current.parent
            current.remove_child(temp_id)
            return find_combination(current, orders, node_id, "y")


x = find_combination(start, stack, start_id)

print x[1]

order_list = [order[:-1] for order in order_list]

for iets in x[1]:
    if iets in order_list:
        order_list.remove(iets)
    iets[0], iets[1] = iets[1], iets[0]
    if iets in order_list:
        order_list.remove(iets)

print order_list

stack = [[w, w[0] * w[1]] for w in order_list]
areas = [order[1] for order in stack]
total_area_to_fill = [sum(areas)]

print(total_area_to_fill)

stack = sorted(stack, key=get_key, reverse=True)

# create starting node and add itself to used nodes
start = Node(start_id, stack.pop(0))
start.add_used_node(start)

x = find_combination(start, stack, start_id)

print x[1]

for iets in x[1]:
    if iets in order_list:
        order_list.remove(iets)
    iets[0], iets[1] = iets[1], iets[0]
    if iets in order_list:
        order_list.remove(iets)

print order_list

stack = [[w, w[0] * w[1]] for w in order_list]
areas = [order[1] for order in stack]
total_area_to_fill.append(sum(areas))

print(total_area_to_fill)
