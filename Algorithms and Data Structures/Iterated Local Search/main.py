from Functions import *
from Algoritms import *
from Visualization import Visualize_Graph

file = open('data.txt', 'w')
file.write(str(500) + '\n')
for i in range(1, 501):
    file.write(str(i) + ' ' + str(randint(0, 500)) + ' ' + str(randint(0, 500)) + '\n')
file.close()

dots_num, dots, distances = Read_File()
Visualize_Graph(dots, IteratedLocalSearch(Greedy(distances), distances))
