# All files and directories ending with .txt and that don't begin with a dot:
import os
import pandas as pd
#Get the list of all files and directories

path = "H://sir zeeshan work//test//0"
dir_list = os.listdir(path)
 
#print("Files and directories in '", path, "' :")
 
# Length of directory
# print(len(dir_list))

#Greater loop to go through each file name
for files in dir_list:
  #print(files)
  pass

# 2) Reading the excel file


data = pd.read_csv('H:/sir zeeshan work/test/0/49114_ortho_1-1_1n_s_il011_2017_1.csv')

# print(data)
# ##################################################

# converting column data to list
longitude= data['longitude'].tolist()
latitude = data['latitude'].tolist()
date = data['date'].tolist()
NDVI = data['NDVI'].tolist()
product = data['product'].tolist()

 
#printing list data
print('longitude : ', longitude)
print('latitude: ', latitude)
print('date :', date)
print('NDVI :', NDVI)
print('product :', product)