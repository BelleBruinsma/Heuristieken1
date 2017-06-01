############################################
#
# PLEASE ADJUST VALUES IN depth_first.py TO GET THIS WORKING
#
# working values that give decent results are:
# threshold = 2720
# max_value_percentage = 95
#
############################################

from depth_first import *

threshold = 2750
min_percentage = 95
min_value = (threshold/100) * min_percentage

order_list = [[34, 18, 1], [33, 14, 1], [32, 10, 1], [30, 19, 1], [29, 12, 1], [29, 11, 1], [27, 19, 1], [27, 11, 1],
              [25, 17, 1], [22, 11, 1], [22, 7, 1], [20, 10, 1], [18, 17, 1], [17, 12, 1], [16, 12, 1], [16, 9, 1],
              [16, 9, 1], [13, 4, 1], [12, 9, 1], [10, 9, 1]]

stack = [[w, w[0] * w[1]] for w in order_list]
areas = [order[1] for order in stack]
total_area_to_fill = sum(areas)

start_stuff = initialize(order_list, "n")
print(start_stuff[1])

while total_area_to_fill > threshold:
    x = find_combination(start_stuff[0], start_stuff[1], start_id)
    order_list = prepare(order_list, x)
    print(order_list)
    start_stuff = initialize(order_list)
    stack = [[w, w[0] * w[1]] for w in order_list]
    areas = [order[1] for order in stack]
    total_area_to_fill = sum(areas)
    print(total_area_to_fill)
