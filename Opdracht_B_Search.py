from depth_first import *

order_list = [[15, 15, 1], [5, 11, 1], [16, 27, 1], [13, 27, 1], [13, 13, 1], [19, 16, 1], [20, 19, 1], [17, 24, 1],

              [11, 22, 1], [11, 14, 1], [7, 23, 1], [14, 17, 1], [16, 24, 1], [20, 13, 1], [15, 10, 1], [19, 22, 1],

              [6, 15, 1], [4, 24, 1],



              # order 3

              [11, 10, 1], [13, 24, 1], [13, 22, 1], [9, 16, 1], [4, 10, 1], [5, 14, 1], [15, 25, 1], [7, 20, 1],

              [16, 12, 1], [12, 12, 1],

              [10, 19, 1], [19, 24, 1], [12, 27, 1], [6, 13, 1], [16, 23, 1], [17, 17, 1], [20, 17, 1], [9, 21, 1],

              [6, 19, 1],

              [12, 18, 1], [11, 19, 1], [18, 27, 1], [16, 12, 1], [16, 10, 1],



              # order 4

              [9, 22, 1], [11, 26, 1], [8, 12, 1], [8, 28, 1], [5, 28, 1], [8, 27, 1], [16, 19, 1], [4, 19, 1],

              [9, 25, 1], [18, 21, 1],

              [18, 25, 1], [11, 16, 1], [17, 27, 1], [11, 27, 1], [8, 14, 1], [10, 27, 1], [14, 21, 1], [12, 20, 1],

              [12, 15, 1]]

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


