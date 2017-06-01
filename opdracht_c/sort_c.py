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