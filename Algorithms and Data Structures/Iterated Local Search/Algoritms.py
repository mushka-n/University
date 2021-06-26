from random import randint


def Greedy(distances):
    dots_num = len(distances)
    curr_dot = 0
    path = [0]
    next_id = 0
    for i in range(dots_num - 1):
        neighbour_min = max(distances[curr_dot])
        for ii in range(dots_num):
            if distances[curr_dot][ii] <= neighbour_min and ii not in path:
                neighbour_min = distances[curr_dot][ii]
                next_id = ii
        path.append(next_id)
        curr_dot = next_id
    return list(map(lambda x: x + 1, path)) + [1]


def two_opt(path):
    node1 = randint(1, len(path) - 3)
    node2 = randint(node1, len(path) - 2)
    path = path[:node1] + path[node1:node2][::-1] + path[node2:]
    return path


def Count_Cost(path, distances):
    total_cost = 0
    for i in range(len(path) - 1):
        cost = distances[path[i] - 1][path[i + 1] - 1]
        total_cost += cost
    return total_cost


def IteratedLocalSearch(path, distances):
    best_cost = Count_Cost(path, distances)
    best_path = path
    print("Start:", best_cost)
    for i in range(1000000):
        new_path = two_opt(best_path)
        new_cost = Count_Cost(new_path, distances)
        if new_cost < best_cost:
            best_path = new_path
            best_cost = new_cost
            print("New leader: ", best_cost, '\n', best_path, sep='')
    print("Winner:", best_cost)
    return best_path
