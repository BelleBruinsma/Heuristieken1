order_list = [[34, 18, 1], [33, 14, 1], [32, 10, 1], [30, 19, 1], [29, 12, 1], [29, 11, 1], [27, 19, 1], [27, 11, 1],
              [25, 17, 1], [22, 11, 1], [22, 7, 1], [20, 10, 1], [18, 17, 1], [17, 12, 1], [16, 12, 1], [16, 9, 1],
              [16, 9, 1], [13, 4, 1], [12, 9, 1], [10, 9, 1]]

def sort_area(list):
    sortedList = sorted(list, key=lambda order: (order[0]*order[1]))
    return sortedList

def sort_width(list):
	sortedList = sorted(list, key=lambda order: (order[1]), reverse=True)
	return sortedList

def sort_height(list):
	sortedList = sorted(list, key=lambda order: (order[0]), reverse=True)
	return sortedList

# sort by perimeter
def sort_peri(list):
    sortedList = sorted(list, key=lambda order: (order[0]+order[1]), reverse=True)
    return sortedList

# sort by ratio
def sort_ratio(list):
    sortedList = sorted(list, key=lambda order: (order[0]/order[1]), reverse=True)
    return sortedList
