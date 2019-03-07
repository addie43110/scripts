import os
import shutil
import sys
from os import path


PATH_TO_SDS = 1


def rename_student_dirs(path_to_sds):

  # go to each student directory and get rid of space, commas, and parentheses
  for subdir in os.listdir(path_to_sds):

    print("\n\nprocessing: " + subdir)
    # go into studentdirectories
    os.chdir(os.path.join(path_to_sds))

    new_name = subdir.replace(" ", "")
    new_name = new_name.replace("(","")
    new_name = new_name.replace(")","")
    new_name = new_name.replace(",", "")
    try:
      os.rename(subdir, new_name)
    except FileNotFoundError as fnfe:
      print(fnfe)
      return -1

    # exit subdir
    os.chdir("..")

    # rename submission attachments
    os.chdir(os.path.join(path_to_sds, new_name))
 
    try:
      os.rename("Submission attachment(s)", "subats")
    except FileNotFoundError as fnfe:
      print("Either did not submit attachment or subats already created.")

    # move submission attachments to parent directory

    files = ["add.s", "maths.s", "swap_dynamic.s", "swap_static.s"]
    files = ["subats/"+a for a in files ] 

    for filename in files:
      try:
        shutil.move(filename, ".")
      except FileNotFoundError as fnfe:
        print(filename + " not found.")
      except shutil.Error as se:
        print(filename+ " already exists in parent directory.")

    os.chdir("../..")
    print("student completed.")

def print_help():
  print("python3 rename.py <path to student directory>\n\npath to student directory should be the folder containing all individual student directories")

def main():
  if (len(sys.argv) != 2):
    print_help()
    return -1
  
  rename_student_dirs(sys.argv[PATH_TO_SDS])






if __name__=="__main__":
  main()
