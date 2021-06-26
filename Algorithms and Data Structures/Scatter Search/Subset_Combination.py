from Funs import Count_Cost
from random import choice


def Subset_Combination(subset, RefSet, distances, b1):
    new_combinations = []
    iter = 1
    for refid in subset:
        if refid <= b1:
            iter += 2

    for i in range(iter):
        if len(subset) == 2:
            new_combinations.append(Type_1_Crossover(RefSet[subset[0]], RefSet[subset[1]]))
        elif len(subset) == 3:
            new_combinations.append(
                Type_2_Crossover(RefSet[subset[0]], RefSet[subset[1]], RefSet[subset[2]], distances))
        else:
            new_combinations.append(
                Type_3_Crossover(RefSet[subset[0]], RefSet[subset[1]], RefSet[subset[2]],
                                 RefSet[subset[3]], distances))

    return new_combinations


def Type_1_Crossover(path1, path2):
    new = [path1[0]]
    for i in range(1, len(path1) - 1):
        if path1[i] in new:
            new.append(path2[i])
        elif path2[i] in new:
            new.append(path1[i])
        else:
            new.append(choice([path1[i], path2[i]]))
    new += [path1[-1]]
    return new


def Type_2_Crossover(path1, path2, path3, distances):
    new1 = Type_1_Crossover(path1, path2)
    new2 = Type_1_Crossover(path1, path3)
    new3 = Type_1_Crossover(path2, path3)

    return_new1 = Type_1_Crossover(new1, new2)
    return_new2 = Type_1_Crossover(new1, new3)
    return_new3 = Type_1_Crossover(new2, new3)
    return_new = [return_new1, return_new2, return_new3]

    new_cost = []
    for i in return_new:
        new_cost.append(Count_Cost(i, distances))

    return return_new[new_cost.index(min(new_cost))]


def Type_3_Crossover(path1, path2, path3, path4, distances):
    new1 = Type_2_Crossover(path1, path2, path3, distances)
    new2 = Type_2_Crossover(path1, path2, path4, distances)
    new3 = Type_2_Crossover(path1, path3, path4, distances)
    new4 = Type_2_Crossover(path2, path3, path4, distances)

    return_new1 = Type_2_Crossover(new1, new2, new3, distances)
    return_new2 = Type_2_Crossover(new1, new2, new4, distances)
    return_new3 = Type_2_Crossover(new1, new3, new4, distances)
    return_new4 = Type_2_Crossover(new2, new3, new4, distances)
    return_new = [return_new1, return_new2, return_new3, return_new4]

    new_cost = []
    for i in return_new:
        new_cost.append(Count_Cost(i, distances))

    return return_new[new_cost.index(min(new_cost))]
