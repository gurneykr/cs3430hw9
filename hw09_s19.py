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
    for sec,info in bee_info_array.items():
        seconds.append(sec)
        upward.append(info[0])
        downward.append(info[1])
        lateral.append(info[2])

    fig1 = plt.figure(1)
    fig1.suptitle('Bee Traffic for'+ csv_fp)
    plt.xlabel('t(seconds)')
    plt.ylabel('Moving Bees')
    plt.ylim([0, 3.0])
    plt.xlim([4.0, 29])
    plt.grid()

    plt.plot(seconds, upward, label='upward', c='r')
    plt.plot(seconds, downward, label='downward', c='g')
    plt.plot(seconds, lateral, label='lateral', c='b')

    plt.legend(loc='best')
    plt.show()

def midpoint_rule(fexpr, a, b, n):
    area = 0
    partition = (b - a)/ n

    for i in np.arange(a, b, partition):
        mid = i + (partition / 2)
        area += fexpr(mid) * partition

    return area

def trapezoidal_rule(fexpr, a, b, n):
    area = 0
    partition = (b - a)/ n

    for i in np.arange(a, b, partition):
        area += partition * ((fexpr(i)+fexpr(i+partition))/2)

    return area

# def sr_approx(fexpr, a, b, n):
#     #Simpson = (2M+T)/3
#     T = trapezoidal_rule(fexpr, a, b, n)
#     M = midpoint_rule(fexpr, a, b, n)
#
#     return (2*M + T)/3

# def sr_approx(fexpr, a, b, n):
#     h = (b - a)/n
#     k = 0.0
#     x = a + h
#     for i in np.arange(1, (n/2) +1):
#         k += 4*fexpr(x)
#         x += 2*h
#
#     x = a + 2*h
#     for i in np.arange(1, n/2):
#         k += 2*fexpr(x)
#         x += 2*h
#
#     return (h/3)*(fexpr(a)+fexpr(b)+k)
# def sr_approx(f, a, b, n):
#     h=(b-a)/n
#     k=0.0
#     x=a + h
#     for i in np.arange(1,n/2 + 1):
#         k += 4*f(x)
#         x += 2*h
#
#     x = a + 2*h
#     for i in np.arange(1,n/2):
#         k += 2*f(x)
#         x += 2*h
#     return (h/3)*(f(a)+f(b)+k)

# def sr_approx(f, a, b, n):
#     partition = (b - a)/n
#     sum = 0
#     for i in range(1, n, 2):
#         sum += 4 * f(a + i * partition)
#     for i in range(2, n - 1, 2):
#         sum += 2 * f(a + i * partition)
#
#     return sum * partition / 3
def sr_approx(fexpr, a, b, n):
    partition = (b - a)/n
    count = 0
    sum = 0
    first = 0
    last = 0

    for i in np.arange(a, b, partition):
        if count == 0:
            # first = fexpr(a+(i*partition))
            first = fexpr(a)
            # print('first: ',first)
        elif count == n:
            last = fexpr(b)
            # print('last: ',last)
        elif count % 2== 0: #multiply evens by 2
            # sum += 2*(fexpr(a+(i*partition)))
            sum += 2 * fexpr(i)
        else:#multiply odds by 4
            sum += 4*fexpr(i)
        count += 1
    return (partition/3)*(first+sum+last)



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
    down_bte = make_bee_traffic_estimator(FD, 'd')
    lat_bte = make_bee_traffic_estimator(FD, 'l')
    print(sr_approx(up_bte, 5, 28, 23))
    print(sr_approx(down_bte, 5, 28, 23))
    print(sr_approx(lat_bte, 5, 28, 23))

import numpy as np
def bee_traffic_stats(fd):
    ## your code here
    pass

def find_smallest_up_down_gap_file(csv_dir):
    ## your code here
    pass

def find_largest_up_down_gap_file(csv_dir):
    ## your code here
    pass

############################

def find_max_up_file(csv_dir):
    ## your code here
    pass

def find_min_up_file(csv_dir):
    ## your code here
    pass

###########################

def find_max_down_file(csv_dir):
    ## your code here
    pass

def find_min_down_file(csv_dir):
    ## your code here
    pass

############################

def find_max_lat_file(csv_dir):
    ## your code here
    pass

def find_min_lat_file(csv_dir):
    ## your code here
    pass
