import itertools
from classes import *


def make_list(values):
    values.reverse()
    attempt_list = [list(i) for i in itertools.product([0, 1], repeat=len(values))]
    for current_combo in attempt_list:
        for current_member in range(len(values)):
            if current_combo[current_member] == 0:
                current_combo[current_member] = [values[current_member][0], values[current_member][1]]
            else:
                current_combo[current_member] = [values[current_member][1], values[current_member][0]]
    return attempt_list


def try_combo(combo, plate):
    start_nr = 1

    for rect in combo:
        u = 1
        while u < len(plate.opt_cord) and len(plate.opt_cord) > 1:
            if plate.opt_cord[u - 1][0] >= plate.opt_cord[u][0] and plate.opt_cord[u - 1][1] >= plate.opt_cord[u][1]:
                plate.opt_cord[u - 1:u + 1] = [[plate.opt_cord[u - 1][0], plate.opt_cord[u - 1][1]]]
                u = 1
            elif plate.opt_cord[u - 1][1] >= plate.opt_cord[u][1]:
                plate.opt_cord[u - 1:u + 1] = [[plate.opt_cord[u][0], plate.opt_cord[u - 1][1]]]
                u = 1
            elif plate.opt_cord[u - 1][0] >= plate.opt_cord[u][0]:
                plate.opt_cord[u - 1:u + 1] = [[plate.opt_cord[u - 1][0], plate.opt_cord[u][1]]]
                u = 1
            else:
                u += 1
        for new_opt in plate.opt_cord:
            if new_opt[0] - rect[0] >= 0 and new_opt[1] + rect[1] <= plate.width:
                before = np.count_nonzero(plate.state) + (rect[1] * rect[0])
                plate.state[new_opt[0] - rect[0]:new_opt[0], new_opt[1]:new_opt[1] + rect[1]] = start_nr
                start_nr += 1
                i = plate.opt_cord.index(new_opt)
                plate.opt_cord[i:i+1] = [new_opt[0] - rect[0], new_opt[1]], [new_opt[0], new_opt[1] + rect[1]]
                if before - np.count_nonzero(plate.state) != 0:
                    return False
                break
            elif new_opt == plate.opt_cord[-1]:
                #print("Nope :'(")
                return False
    return True, combo
