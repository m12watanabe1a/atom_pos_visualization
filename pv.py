import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import sys
import argparse

HEADER_ROWS = 3

molecular_type = 0.0
molecular_num = 0
scene_num = 0
x_field_size = 0.0
y_field_size = 0.0
z_field_size = 0.0
time_init = 0.0
time_step = 0.0

x_list = None
y_list = None
z_list = None

scat = None

def read_header(filename):
    global molecular_type, molecular_num, scene_num
    global x_field_size, y_field_size, z_field_size
    global time_init, time_step

    with open(filename) as f:
        molecular_type, molecular_num, scene_num = [float(s) for s in f.readline().split()]
        x_field_size, y_field_size, z_field_size = [float(s) for s in f.readline().split()]
        time_init, time_step = [float(s) for s in f.readline().split()]


def read_rows(filename):
    global HEADER_ROWS
    global x_list, y_list, z_list

    data = np.loadtxt(filename, skiprows = HEADER_ROWS)
    x_list = data[:,0]
    y_list = data[:,1]
    z_list = data[:,2]


def init():
    global scat

    return scat,


def update(frame):
    global molecular_num
    global x_list, y_list, z_list
    global scat

    index_from = int(frame*molecular_num)
    index_to = int((frame + 1)*molecular_num)

    x = x_list[index_from:index_to]
    y = y_list[index_from:index_to]
    z = z_list[index_from:index_to]

    scat.set_data(x, y)
    scat.set_3d_properties(z)

    return scat,


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="please set dat file", type=str)
    parser.add_argument("--save", help="optional", action="store_true")
    args = parser.parse_args()

    return(args)

def main():
    global scat
    args = get_args()
    if not hasattr(args, 'filename'):
        print('filename is not given')
        return
    filename = args.filename

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    read_header(filename)
    read_rows(filename)

    ax.set_xlim(0, x_field_size)
    ax.set_ylim(0, y_field_size)
    ax.set_zlim(0, z_field_size)

    scat, = ax.plot([], [], [], marker="o", alpha = 0.8, markersize=4, linestyle='None')

    anime = animation.FuncAnimation(fig = fig, func = update, frames = int(scene_num) , interval = 100, init_func = init, blit = True, repeat = False)

    if args.save:
        anime.save('MD.gif', writer = "imagemagick")

    plt.show()
    return

if __name__ == "__main__":
    main()
