#!/usr/bin/python

####################################
# module: hw09_s19.py
# YOUR NAME
# YOUR A#
####################################


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
    reader.next() #to skip the header
    for row in reader:
      secs, up, down, lat = int(row[0]), float(row[1]), \
                            float(row[2]), float(row[3])
      fd[secs] = (up, down, lat)
    return fd

def plot_bee_traffic(csv_fp):
  ## your code here
  pass

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


  