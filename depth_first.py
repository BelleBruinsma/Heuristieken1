import sys
from combination_check import *
sys.setrecursionlimit(100000)

# initialize global variables
area_list = []
start_id = 0
final_item_list = []
threshold = 2600
min_percentage = 90
# threshold = 2720
# min_percentage = 95
min_value = (threshold/100) * min_percentage
final_total_areas = []
bliep = 0


def initialize(order_list, sort="y"):
    # calculate and add area to order list
    stack = [[w, w[0] * w[1]] for w in order_list]
    areas = [order[1] for order in stack]
    total_area_to_fill = sum(areas)

    # sort the order list by height
    if sort == "y":
        stack = sorted(stack, key=get_key, reverse=True)

    # create starting node and add itself to used nodes
    start = Node(start_id, stack.pop(0))
    start.add_used_node(start)
    return start, stack, total_area_to_fill


# key generator based in height for sorting
def get_key(item):
    return item[1]


# recursive function that searches for combination of areas where no more rectangle can be added without exceeding
# the area of the used bins
def find_combination(current, orders, node_id, checked="n"):
    global bliep
    global min_value
    # will be run at the first iteration of the function
    if not checked == "y":
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
            total = 0
            for cur in attempt_list[0]:
                total += cur[0] * cur[1]
            if total >= min_value:
                for attempt in attempt_list:
                    test_plate = Plate(50, 60, 1)
                    h = try_combo(attempt, test_plate)
                    if h:
                        return True, h[1]
            # if combination didn't work, backtrack and remove last checked node from children
            bliep += 1
            print(bliep)
            temp_id = current.id
            current.parent.add_used_node(current)
            new = current.parent
            new.remove_child(temp_id)
            del current
            return find_combination(new, orders, node_id, "y")


def prepare(old_list, x):
    if len(old_list[0]) == 3:
        old_list = [order[:-1] for order in old_list]
    for iets in x[1]:
        if iets in old_list:
            old_list.remove(iets)
        iets[0], iets[1] = iets[1], iets[0]
        if iets in old_list:
            old_list.remove(iets)
    return old_list

# start_stuff = initialize(order_list, "n")
# x = find_combination(start_stuff[0], start_stuff[1], start_id)
# order_list = prepare(order_list, x)
# print(order_list)
# start_stuff = initialize(order_list)
# x = find_combination(start_stuff[0], start_stuff[1], start_id)
# order_list = prepare(order_list, x)
# print(order_list)
# start_stuff = initialize(order_list)



# stack = sorted(stack, key=get_key, reverse=True)
#
# # create starting node and add itself to used nodes
# start = Node(start_id, stack.pop(0))
# start.add_used_node(start)
#
# #x = find_combination(start, stack, start_id)
#
# print(x[1])
#
# for iets in x[1]:
#     if iets in order_list:
#         order_list.remove(iets)
#     iets[0], iets[1] = iets[1], iets[0]
#     if iets in order_list:
#         order_list.remove(iets)
#
# print(order_list)

#x = find_combination(start, stack, start_id)
