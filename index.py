# All files and directories ending with .txt and that don't begin with a dot:
import os
import pandas as pd
#Get the list of all files and directories

path = "H://sir zeeshan work//test//0"
dir_list = os.listdir(path)
 
#print("Files and directories in '", path, "' :")

# Length of directory
print(len(dir_list))
length = len(dir_list)

import numpy as np

#Greater loop to go through each file name
count=0
Greater_Longitude=[]
Greater_Latitude = []
Greater_Date = []
Greater_NDVI = []
Greater_Product = []

############################################We are inside the loop.Get ready the loop is going to start
for files in dir_list:
  #print(files)
  data = pd.read_csv('H:/sir zeeshan work/test/0/'+str(files), encoding="ISO-8859-1")
  #print(files)
  
  longitude= data['longitude'].tolist()
  latitude = data['latitude'].tolist()
  date = data['date'].tolist()
  NDVI = data['NDVI'].tolist()
  product = data['product'].tolist()
  #########################APPENDING THE DATA#######################################
  Greater_Longitude.append(longitude)
  Greater_Latitude.append(latitude)
  Greater_Date.append(date)
  Greater_NDVI.append(NDVI)
  Greater_Product.append(product)
  
  #Printing the count to know at which length the memory leak is occuring
  #print("Count =====================> ",count)

  #Breaking the loop to avoid memory leak when the files length available in the folder or directory are reached.Discovered to avoid memory leak
  count = count + 1
  if(count==length-1):
      break
############################################The loop Ended Successfully.Done

# 2) Reading the excel file

#####################################STOP#########################################################
# data = pd.read_csv('H:/sir zeeshan work/test/0/49114_ortho_1-1_1n_s_il011_2017_1.csv')

# # print(data)
# # ##################################################

# # converting column data to list
# longitude= data['longitude'].tolist()
# latitude = data['latitude'].tolist()
# date = data['date'].tolist()
# NDVI = data['NDVI'].tolist()
# product = data['product'].tolist()

#Merging all arrays
Greater_Longitude_Combine = np.concatenate((Greater_Longitude))
 
# #printing list data
print('longitude : ',len(Greater_Longitude_Combine))
# print('latitude: ', latitude)
# print('date :', date)
# print('NDVI :', NDVI)
# print('product :', product)