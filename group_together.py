import os
import shutil
import sys


'''note that this is the order of the marks as well.'''
ADD           = 1
MATH          = 2
SWAP_STATIC   = 3
SWAP_DYNAMIC  = 4

def read_in_files(file_list):
  
  # read the marks from all the outputs
  for filename in file_list:
    with open(filename) as f:
      contents = f.read()
    
    contents = contents.splitlines()
    contents = [line.split(',') for line in contents]
    if filename=='add_output.txt':
      contents = [[name, 'a: '+mark] for [name,mark] in contents]
      result = contents
    else:
      contents = [ mark for [name, mark] in contents]
      result = [prev+[new_mark] for (prev, new_mark) in  zip(result, contents)]

  # sort contents by name
  result.sort(key = sortByName)

  # print results
  for student in result:
    print(str(student))


def sortByName(val):
  return val[0]

def print_help():
  print("USAGE: python3.6 group_together.py <add outfile> <math outfile> <swap_static outfile> <swap_dynamic outfile>")

def main():
  if len(sys.argv)<5:
    print_help()
    return -1

  read_in_files([sys.argv[ADD], sys.argv[MATH], sys.argv[SWAP_STATIC], sys.argv[SWAP_DYNAMIC]])

if __name__=="__main__":
  main()

