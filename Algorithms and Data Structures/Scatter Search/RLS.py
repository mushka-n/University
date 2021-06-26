from random import randint


def Two_Opt(path):
    node1 = randint(1, len(path) - 3)
    node2 = randint(node1, len(path) - 2)
    path = path[:node1] + path[node1:node2][::-1] + path[node2:]
    return path


def Random_Local_Search(path, distances):
    best_cost = Count_Cost(path, distances)
    best_path = path
    for i in range(randint(100, 1000)):
        new_path = Two_Opt(best_path)
        new_cost = Count_Cost(new_path, distances)
        if new_cost < best_cost:
            best_path = new_path
            best_cost = new_cost
    return best_path


def Count_Cost(path, distances):
    total_cost = 0
    for i in range(len(path) - 1):
        cost = distances[path[i]][path[i + 1]]
        total_cost += cost
    return total_cost
