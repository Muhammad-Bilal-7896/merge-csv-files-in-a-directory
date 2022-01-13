#To read all files in a directory

# import glob

# txtfiles = []
# for file in glob.glob("*.txt"):
#     txtfiles.append(file)


# All files and directories ending with .txt and that don't begin with a dot:
import os
 
# Get the list of all files and directories

path = "H://sir zeeshan work//test//0"
dir_list = os.listdir(path)
 
print("Files and directories in '", path, "' :")
 
# Length of directory
print(len(dir_list))

#Greater loop to go through each file name
for files in dir_list:
  print(files)

  