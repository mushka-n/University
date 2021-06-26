import pandas as pd
from Subset_Generation import *
from Subset_Combination import Subset_Combination
from Funs import *
import Dot

# Чтение из файла
data = pd.read_csv('cities.csv', sep=',').to_numpy().tolist()
print('Data file is read')

# Заполнение массива с точками
dots = []
for row in data[:1000]:
    dots.append(Dot.Dot(row[0], row[1], row[2]))
dots_num = len(dots)
print('Dots list is filled')

# Заполнение массива с расстояниями
distances = Fill_Distances(dots)
print('Distances list is filled')

# Константы и объявление популяций
P, PSize = [], 180
RefSet, RefSetSize = [], 18
b1, b2 = 6, 12

# Создаем первую популяцию и улучшаем ее с помощью нескольких итераций Two_Opt
for i in range(PSize):
    P.append(Semi_Greedy_Path(distances))
    P[i] = Random_Local_Search(P[i], distances)
print('Population is created and modified')

# Заполняем матрицу схожести
similarity_matrix = Fill_Similarity_Matrix(P)
print('First similarity matrix is filled')

# Заполняем RefSet
RefSet += P[:b1]
RefIds = list(range(b1))
while len(RefSet) < (b1 + b2):
    new_id = randint(b1, PSize - 1)
    new_ref = P[new_id]
    if new_id not in RefIds:
        RefIds.append(new_id)
        RefSet.append(new_ref)
RefIds = range(b1 + b2)
print('RefSet is filled')

# Заполняем список со стоимостью каждого пути
cost_list = []
for person in RefSet:
    cost_list.append(Count_Cost(person, distances))
print('Cost list is filled')

# Сортируем P и список стоимостей от меньшего к большему
RefSet, cost_list = Sort_RefSet(RefSet, cost_list)
print('RefSet and cost list are sorted')

for i in range(len(cost_list)):
    print(cost_list[i], RefSet[i])

for i in range(1):
    subsets = Generate_Subsets(b1, b2)
    for subset in subsets:
        combined_subset = Subset_Combination(subset, RefSet, distances, b1)
        RefSet = RefSet_Update(RefSet, cost_list, combined_subset, distances)

for i in range(len(cost_list)):
    print(cost_list[i], RefSet[i])
