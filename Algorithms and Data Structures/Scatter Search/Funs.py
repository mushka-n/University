from scipy.spatial import distance
from random import choice
from RLS import *
import numpy as np


def Fill_Distances(dots):
    dots_num = len(dots)
    distances = [[]] * dots_num

    for i in range(dots_num):
        dot_distances = []
        for j in range(dots_num):
            dot_distances.append(round(distance.euclidean(dots[i].Position(), dots[j].Position())))
            # dot_distances.append(distance.euclidean(dots[i].Position(), dots[j].Position()))
        distances[i] = dot_distances
    return distances


def Semi_Greedy_Path(distances):
    dots_num = len(distances)
    all_ids = range(dots_num)
    semigreedy_path = [0]

    for i in range(dots_num - 1):
        last_point = semigreedy_path[-1]
        last_point_distances = distances[last_point]

        # C шансом 0.35 выбирается самый жадный путь
        if randint(1, 100) > 65:
            neighbour_min = max(last_point_distances)
            next_id = 0
            for ii in range(dots_num):
                if (0 < last_point_distances[ii] <= neighbour_min) and (ii not in semigreedy_path):
                    neighbour_min = last_point_distances[ii]
                    next_id = ii
            if not next_id:
                next_id = last_point_distances.index(neighbour_min)

        # C шансом 0.65 выбирается случайный из тех что меньше среднего арифметического расстояния
        # Если все такие значения уже в пути - выбираем случайное из оставшихся
        else:
            mean_distance = np.mean(last_point_distances) * dots_num / (dots_num - 1)
            less_then_mean = []

            for ii in range(dots_num):
                if (0 < last_point_distances[ii] < mean_distance) \
                        and (ii not in semigreedy_path):
                    less_then_mean.append(ii)

            if less_then_mean:
                next_id = less_then_mean[randint(0, len(less_then_mean) - 1)]
            else:
                not_visited_ids = list(set(all_ids) - set(semigreedy_path))
                next_id = not_visited_ids[randint(0, len(not_visited_ids) - 1)]

        semigreedy_path.append(next_id)

    return semigreedy_path + [semigreedy_path[0]]


def Count_Similarity(path1, path2):
    similarity = 0
    for i in range(len(path1)):
        if path1[i] == path2[i]:
            similarity += 1
    return similarity


def Fill_Similarity_Matrix(P):
    similarity_matrix = []
    for i in P:
        similarities = []
        for j in P:
            similarities.append(Count_Similarity(i, j))
        similarity_matrix.append(similarities)
    return similarity_matrix


def Quick_Sort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = choice(nums)
    l_nums = [n for n in nums if n < q]
    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if n > q]
    return Quick_Sort(l_nums) + e_nums + Quick_Sort(b_nums)


def Sort_RefSet(RefSet, cost_list):
    sorted_P, sorted_cost_list = [], Quick_Sort(cost_list)
    for cost in sorted_cost_list:
        old_index = cost_list.index(cost)
        sorted_P.append(RefSet[old_index])
    return sorted_P, sorted_cost_list


def RefSet_Update(RefSet, cost_list, subsets, distances):
    for subset in subsets:
        new_cost = Count_Cost(subset, distances)
        print(new_cost)
        if new_cost < cost_list[-1]:
            for i in range(len(cost_list)):
                if cost_list[i] < new_cost:
                    RefSet[i], cost_list[i] = subset, new_cost
                    cost_list.pop()
                    RefSet.pop()
    return RefSet
