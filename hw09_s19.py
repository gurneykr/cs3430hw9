#!/usr/bin/python

####################################
# module: hw09_s19.py
# Krista Gurney
# A01671888
####################################

import csv
import os
import matplotlib.pyplot as plt
import numpy as np
import glob

def generate_file_names(ftype, rootdir):
    '''
    recursively walk dir tree beginning from rootdir
    and generate full paths to all files that end with ftype.
    sample call: generate_file_names('.jpg', /home/pi/images/')
    '''
    for path, dirlist, filelist in os.walk(rootdir):
        for file_name in filelist:
            if not file_name.startswith('.') and \
               file_name.endswith(ftype):
                yield os.path.join(path, file_name)
        for d in dirlist:
            generate_file_names(ftype, d)

def display_csv_file(csv_file_path):
    fd = {}
    with open(csv_file_path, 'r') as instream:
        reader = csv.reader(instream, delimiter = ",")
        for row in reader:
            print(row)

def read_csv_file(csv_file_path):
    fd = {}
    with open(csv_file_path, 'r') as instream:
        reader = csv.reader(instream, delimiter = ",")
        # reader.next() #to skip the header
        line_count = 0
        for row in reader:
            if line_count > 0:
                secs, up, down, lat = int(row[0]), float(row[1]), \
                                    float(row[2]), float(row[3])
                fd[secs] = (up, down, lat)
            else:
                line_count += 1
        return fd

def plot_bee_traffic(csv_fp):
    bee_info_array = read_csv_file(csv_fp)
    seconds = []
    upward = []
    downward = []
    lateral = []
    max_val = 0
    for sec, info in bee_info_array.items():
        seconds.append(sec)
        upward.append(info[0])
        downward.append(info[1])
        lateral.append(info[2])
        if info[0] > max_val:
            max_val = info[0]
        if info[1] > max_val:
            max_val = info[1]
        if info[2] > max_val:
            max_val = info[2]

    fig1 = plt.figure(1)
    fig1.suptitle('Bee Traffic for'+ csv_fp)
    plt.xlabel('t(seconds)')
    plt.ylabel('Moving Bees')
    plt.ylim([0, max_val])
    plt.xlim([2, 30])
    plt.grid()

    plt.plot(seconds, upward, label='upward', c='r')
    plt.plot(seconds, downward, label='downward', c='g')
    plt.plot(seconds, lateral, label='lateral', c='b')

    plt.legend(loc='best')
    plt.show()

def sr_approx(fexpr, a, b, n):
    partition = (b - a)/n
    count = 0
    sum = 0

    for i in np.arange(a, b+partition, partition):
        # x = a+(i*partition)
        if count == 0 or count == n:
            sum += fexpr(i)
        elif count % 2 == 0: # multiply evens by 2
            sum += 2 * fexpr(i)
        else:               # multiply odds by 4
            sum += 4*fexpr(i)
        count += 1
    return (1/3)*partition*sum


def bee_traffic_estimate(t, md='u', fd={}):
    assert md == 'u' or md == 'd' or md == 'l'
    vals = fd.get(int(t))
    if vals is None:
        return None
    elif md == 'u':
        return vals[0]
    elif md == 'd':
        return vals[1]
    elif md == 'l':
        return vals[2]

def make_bee_traffic_estimator(fd, md):
    assert md == 'u' or md == 'd' or md == 'l'
    return lambda t: bee_traffic_estimate(t, md=md, fd=fd)

def test(csv_fp):
    FD = read_csv_file(csv_fp)
    up_bte = make_bee_traffic_estimator(FD, 'u')
    # print("up_bte: ",up_bte)
    down_bte = make_bee_traffic_estimator(FD, 'd')
    lat_bte = make_bee_traffic_estimator(FD, 'l')
    print(sr_approx(up_bte, 5, 28, 23))
    print(sr_approx(down_bte, 5, 28, 23))
    print(sr_approx(lat_bte, 5, 28, 23))

import numpy as np
def bee_traffic_stats(fd):
    up_bte = make_bee_traffic_estimator(fd, 'u')
    # print("up_bte: ",up_bte)
    down_bte = make_bee_traffic_estimator(fd, 'd')
    lat_bte = make_bee_traffic_estimator(fd, 'l')
    up = sr_approx(up_bte, 5, 28, 23)
    down = sr_approx(down_bte, 5, 28, 23)
    lat = sr_approx(lat_bte, 5, 28, 23)

    return (up, down, lat)

def test_smallest_up_down_gap(csv_dir):
    fp, u, d, l, gap = find_smallest_up_down_gap_file(csv_dir)
    print(fp, u, d, l, gap)
    plot_bee_traffic(fp)

def find_smallest_up_down_gap_file(csv_dir):
    path = csv_dir+"/*.csv"
    current_gap = 1000000000
    info = ()
    for file in glob.glob(path):
        # print(file)
        fd = read_csv_file(file)
        stats = bee_traffic_stats(fd)
        gap = abs(stats[0] - stats[1])#estimate gap
        if gap < current_gap:
            current_gap = gap
            info = (file, *stats, gap)

    return info

def test_largest_up_down_gap(csv_dir):
    fp, u, d, l, gap = find_largest_up_down_gap_file(csv_dir)
    print(fp, u, d, l, gap)
    plot_bee_traffic(fp)

def find_largest_up_down_gap_file(csv_dir):
    path = csv_dir+"/*.csv"
    current_gap = 0
    info = ()
    for file in glob.glob(path):
        fd = read_csv_file(file)
        stats = bee_traffic_stats(fd)
        gap = abs(stats[0] - stats[1])#estimate gap
        if gap > current_gap:
            current_gap = gap
            info = (file, *stats, gap)

    return info

############################

def find_max_up_file(csv_dir):
    path = csv_dir + "/*.csv"
    current_up = 0
    info = ()
    for file in glob.glob(path):
        fd = read_csv_file(file)
        stats = bee_traffic_stats(fd)

        if stats[0] > current_up:
            current_up = stats[0]
            info = (file, *stats)

    return info

def test_max_up(csv_dir):
    fp, u, d, l = find_max_up_file(csv_dir)
    print(fp, u, d, l)
    plot_bee_traffic(fp)

def find_min_up_file(csv_dir):
    path = csv_dir + "/*.csv"
    current_up = 10000000
    info = ()
    for file in glob.glob(path):
        fd = read_csv_file(file)
        stats = bee_traffic_stats(fd)

        if stats[0] < current_up:
            current_up = stats[0]
            info = (file, *stats)

    return info

def test_min_up(csv_dir):
    fp, u, d, l = find_min_up_file(csv_dir)
    print(fp, u, d, l)
    plot_bee_traffic(fp)
###########################

def find_max_down_file(csv_dir):
    path = csv_dir + "/*.csv"
    current_down = 0
    info = ()
    for file in glob.glob(path):
        fd = read_csv_file(file)
        stats = bee_traffic_stats(fd)

        if stats[1] > current_down:
            current_down = stats[1]
            info = (file, *stats)

    return info

def test_max_down(csv_dir):
    fp, u, d, l = find_max_down_file(csv_dir)
    print(fp, u, d, l)
    plot_bee_traffic(fp)

def find_min_down_file(csv_dir):
    path = csv_dir + "/*.csv"
    current_down = 10000000
    info = ()
    for file in glob.glob(path):
        fd = read_csv_file(file)
        stats = bee_traffic_stats(fd)

        if stats[1] < current_down:
            current_down = stats[1]
            info = (file, *stats)

    return info

def test_min_down(csv_dir):
    fp, u, d, l = find_min_down_file(csv_dir)
    print(fp, u, d, l)
    plot_bee_traffic(fp)
############################

def find_max_lat_file(csv_dir):
    path = csv_dir + "/*.csv"
    current_lat = 0
    info = ()
    for file in glob.glob(path):
        fd = read_csv_file(file)
        stats = bee_traffic_stats(fd)

        if stats[2] > current_lat:
            current_lat = stats[2]
            info = (file, *stats)

    return info

def test_max_lat(csv_dir):
    fp, u, d, l = find_max_lat_file(csv_dir)
    print(fp, u, d, l)
    plot_bee_traffic(fp)

def find_min_lat_file(csv_dir):
    path = csv_dir + "/*.csv"
    current_lat = 10000000
    info = ()
    for file in glob.glob(path):
        fd = read_csv_file(file)
        stats = bee_traffic_stats(fd)

        if stats[2] < current_lat:
            current_lat = stats[2]
            info = (file, *stats)

    return info

def test_min_lat(csv_dir):
    fp, u, d, l = find_min_lat_file(csv_dir)
    print(fp, u, d, l)
    plot_bee_traffic(fp)
