from celluloid import Camera
from matplotlib import pyplot as plt
import sys

file = open(sys.argv[1], 'r')
figure = plt.figure()
camera = Camera(figure)

if len(sys.argv) < 2:
    print("Usage: python vis.py <filename>")
    exit(-1)

for row in file.readlines()[1:]:
    l = row.split(',')[1:-1]
    xs = list(map(float, l[::2]))
    ys = list(map(float, l[1::2]))
    plt.scatter(xs, ys, color='blue', s=3)
    camera.snap()

camera.animate().save('./visualization/visualization.gif')