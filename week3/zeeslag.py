glasplaat = []

for i in range(5):
    glasplaat.append(["0"] * 6)

def print_glasplaat(glasplaat):
    for row in glasplaat:
        print (" ".join(row))

print_glasplaat(glasplaat)
print("")

current_x = 0
current_y = 0
highest_y = 0

def place_order(width, height):

    global current_x
    global current_y
    global highest_y
    global glasplaat

    if height > highest_y:
        highest_y = height

    if not width + current_x > 6:
        for row in range(current_y, current_y + height):
            for col in range(current_x, current_x + width):
                glasplaat[row][col] = "1"
        current_x += width

    elif not current_y + highest_y + height > 5:
        current_y += highest_y
        highest_y = height

        for row in range(current_y, current_y + height):
            for col in range(width):
                glasplaat[row][col] = "1"

        current_x = width

place_order(2, 3)
place_order(3, 3)
place_order(3, 2)
place_order(1, 2)
place_order(3, 1)
place_order(2, 1)

print_glasplaat(glasplaat)
