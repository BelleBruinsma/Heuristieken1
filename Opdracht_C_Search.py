############################################
#
# NOT YET FUNCTIONAL
#
# Can find way to fill plates with single types of rectangles
# Extension to also fit in plates of a lower tier is almost working
#
############################################


from depth_first import *
node_id = 0
# order_list = [[13, 24], [17, 19], [15, 15], [7, 16], [16, 21], [11, 14], [11, 17], [15, 17], [15, 23], [6, 12],
#                         [16, 15], [16, 24], [7, 16], [12, 23], [14, 12], [13, 24], [9, 18], [15, 23], [10, 15], [8, 18],
#                         [13, 18]]

order_list_2 = [[15, 21, 2], [15, 15, 2], [10, 23, 2], [11, 11, 2], [7, 24, 2], [15, 23, 2], [17, 22, 2], [15, 19, 2],
              [18, 21, 2], [13, 12, 2], [17, 23, 2], [9, 20, 2], [15, 23, 2], [14, 19, 2], [12, 13, 2], [16, 15, 2],
              [11, 10, 2], [8, 19, 2], [8, 23, 2], [7, 18, 2], [7, 11, 2]]

order_list_3 = [[18, 10, 3], [9, 13, 3], [7, 18, 3], [15, 12, 3], [6, 20, 3], [8, 20, 3], [6, 24, 3], [11, 16, 3],
                [12, 24, 3], [11, 17, 3], [15, 23, 3]]

order_list = order_list_3

# orders that were left after running algorithm with order_list_3 (orders of type III)
order_list = [[9, 13], [15, 12], [6, 20], [11, 17]]



stack = [[w, w[0] * w[1]] for w in order_list]
areas = [order[1] for order in stack]
total_area_to_fill = sum(areas)
start_area = order_list[0][0] * order_list[0][1]

start_stuff = initialize(order_list, "n")


# makes the current list the starting point of next search, not yet fully working
start_stuff[0].total_area = start_area
current = start_stuff[0]
while start_stuff[1]:
    current.add_child(Node(node_id, start_stuff[1].pop(0)))
    current.children[0].total_area += current.children[0].area
    current = current.children[0]

current.total_area += current.area
print(current.total_area)
node_id += 1

order_list = order_list_2

# calculate and add area to order list
stack = [[w, w[0] * w[1]] for w in order_list]
areas = [order[1] for order in stack]
total_area_to_fill = sum(areas) + current.total_area

stack = sorted(stack, key=get_key, reverse=True)

# create starting node and add itself to used nodes
start = current
start.add_used_node(start)


# while total_area_to_fill > threshold:
#     x = find_combination(start, stack, start_id)
#     order_list = prepare(order_list, x)
#     print(order_list)
#     start_stuff = initialize(order_list)
#     stack = [[w, w[0] * w[1]] for w in order_list]
#     areas = [order[1] for order in stack]
#     total_area_to_fill = sum(areas)
#     print(total_area_to_fill)
#
