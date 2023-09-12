def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s[0] == 4 and s[1] == 4

def successors(s):
    x, y, z = s
    successors_list = []

    if x > 0 and y < 5:
        amount = min(x, 5 - y)
        new_state = (x - amount, y + amount, z)
        successors_list.append((new_state, amount))

    if x > 0 and z < 3:
        amount = min(x, 3 - z)
        new_state = (x - amount, y, z + amount)
        successors_list.append((new_state, amount))

    if y > 0 and x < 8:
        amount = min(y, 8 - x)
        new_state = (x + amount, y - amount, z)
        successors_list.append((new_state, amount))

    if y > 0 and z < 3:
        amount = min(y, 3 - z)
        new_state = (x, y - amount, z + amount)
        successors_list.append((new_state, amount))

    if z > 0 and x < 8:
        amount = min(z, 8 - x)
        new_state = (x + amount, y, z - amount)
        successors_list.append((new_state, amount))

    if z > 0 and y < 5:
        amount = min(z, 5 - y)
        new_state = (x, y + amount, z - amount)
        successors_list.append((new_state, amount))

    return successors_list
