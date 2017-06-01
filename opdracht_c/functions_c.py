import numpy

# function to find the biggest rectangle of zero's (waste)
def getMaxArea(s):

    nrows = numpy.shape(s)[0]
    ncols = numpy.shape(s)[1]
    skip = 1
    area_max = (0, [])

    a=s
    w = numpy.zeros(dtype=int, shape=a.shape)
    h = numpy.zeros(dtype=int, shape=a.shape)
    for r in range(nrows):
        for c in range(ncols):
            if a[r][c] == skip:
                continue
            if r == 0:
                h[r][c] = 1
            else:
                h[r][c] = h[r-1][c]+1
            if c == 0:
                w[r][c] = 1
            else:
                w[r][c] = w[r][c-1]+1
            minw = w[r][c]
            for dh in range(h[r][c]):
                minw = min(minw, w[r-dh][c])
                area = (dh+1)*minw
                if area > area_max[0]:
                    area_max = (area, [(r-dh, c-minw+1, r, c)])

    area = area_max
    return area


# function to find the coordinates and update the order list
# of the one we took a order from because there was enough room for it
## getAreaSize is beter
def getCoordinates(area):

    topleft = area[1][0][:2]
    bottomright = area[1][0][-2:]
    compute_height = bottomright[0] - topleft[0] + 1
    compute_width = bottomright[1] - topleft[1] + 1
    area_size = [compute_height, compute_width]
    return area_size


def getCleanOrderList(area_size, orderlist):
    compute_height = area_size[0]
    compute_width = area_size[1]

    index_vec = []

    # for every rectangle in the order list, check if it fits the rectangle of waste
    for i in range(len(orderlist)):
        element = orderlist[i]
        index_vec.append(element[0] <= compute_height and element[1] <= compute_width)
    temp = [i for i, x in enumerate(index_vec) if x]
    # remove the rectangle that fits the coordinates

    if len(temp) == 0:
        order_list_clean = orderlist
        deleted_element = []
    else:
        remove_index = min(temp)
        order_list_clean = orderlist[:remove_index] + orderlist[remove_index + 1:]
        deleted_element = orderlist[remove_index]

    return [order_list_clean, deleted_element]

def newPlate(list, waste_order, area_max, category):

    # for every plate of type two, at the biggest rectangle of waste, place the order that fits and change it into nines
    for i in range(0,len(list)):

        coordinates = map(lambda x: x[1][0], area_max)

        largest_rectangle_waste = list[0][coordinates[0][0]:(coordinates[0][2]+1),coordinates[0][1]:(coordinates[0][3]+1)]

        new_temp = list[i]
        new_cor1 = coordinates[i][0] + waste_order[i][0]
        new_cor2 = coordinates[i][1] + waste_order[i][1]

        # change the zeros of the coordinates of the new rectangle into nine
        new_temp[coordinates[i][0]:new_cor1, coordinates[i][1]:new_cor2] += 1

        # for every plate make a new csv file with the changed nines
        numpy.savetxt("plate_" + str(category) + str(i) + "_new.csv", new_temp, delimiter="", fmt='%1.0f')
