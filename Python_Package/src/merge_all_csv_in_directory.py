from ast import Global
from turtle import pos

#################################
def merge_list_of_dictionaries(dict_list):
  new_dict = {}
  for d in dict_list:
    for d_key in d:
      if d_key not in new_dict:
        new_dict[d_key] = []
      new_dict[d_key].append(d[d_key])
  return new_dict

def merge_all_csv_in_directory(path_="C:/"):
    # All files and directories ending with .txt and that don't begin with a dot:
    import numpy as np
    import os
    import pandas as pd
    # Get the list of all files and directories
    # Path Formats
    # H://sir zeeshan work//Coding files//Test
    # H://sir zeeshan work//train//0
    # H://sir zeeshan work//Coding files//Train
    # H://sir zeeshan work//val//0
    # H://sir zeeshan work//Coding files//Val
    path = path_
    dir_list = os.listdir(path)

    # print("Files and directories in '", path, "' :")

    # Length of directory
    print("Length of files in the given path directory is : " + str(len(dir_list)))

    length = len(dir_list)

    # Greater loop to go through each file name
    count = 0
    #Lets make its creation dynamic
    # Greater_Longitude = []
    # Greater_Latitude = []
    # Greater_Date = []
    # Greater_NDVI = []
    # Greater_Product = []
    #Lets make its creation dynamic

    TempCheck = pd.read_csv(path_ +
                           str(dir_list[0]))

    TempColumns = list(TempCheck.head(0))

    length_of_csv_headers = len(TempColumns)

    #print("Reading csv we got ==> ",length_of_csv_headers)

    Global_Array_Of_Data = []

    #Pushing empty arrays
    # for col_names in TempColumns:
    #     print(col_names)
    #     Global_Array_Of_Data.append({ col_names: [] })
  
    print(Global_Array_Of_Data)

    #Will be tested later
    #We are inside the loop.Get ready the loop is going to start
    for files in dir_list:
        # print(files)
        # Path Format: H:/sir zeeshan work/train/0/
        # H:/sir zeeshan work/val/0/
        # H:/sir zeeshan work/Coding files/Val/
        data = pd.read_csv(path_ +
                           str(files))

        #Reading Column Names
        columns = list(data.head(0))

        # Focus here later
        # print("The column names are : ",columns)

        # longitude = data[columns[0]].tolist()
        # latitude = data[columns[1]].tolist()
        # date = data[columns[2]].tolist()
        # NDVI = data[columns[3]].tolist()
        # product = data[columns[4]].tolist()

   

        dynamic_temp_object={}

        temp_count = 0
        for cols in TempColumns:
            dynamic_temp_object[cols]=data[columns[temp_count]].tolist()
            temp_count = temp_count + 1
            # print("Value ===> ",temp_count)
        
        #print("T is ==> ",dynamic_temp_object)

        #Pushing the object in global array after filling it with appropriate key and values
        Global_Array_Of_Data.append(dynamic_temp_object)
                        
        # print(files)

        # longitude = data[columns[0]].tolist()
        # latitude = data[columns[1]].tolist()
        # date = data[columns[2]].tolist()
        # NDVI = data[columns[3]].tolist()
        # product = data[columns[4]].tolist()
        #########################APPENDING THE DATA#######################################
        # Greater_Longitude.append(longitude)
        # Greater_Latitude.append(latitude)
        # Greater_Date.append(date)
        # Greater_NDVI.append(NDVI)
        # Greater_Product.append(product)

        # Printing the count to know at which length the memory leak is occuring
        # print("Count =====================> ",count)

        # Breaking the loop to avoid memory leak when the files length available in the folder or directory are reached.Discovered to avoid memory leak
        count = count + 1
        if(count == 3):
            break
    # The loop Ended Successfully.Done

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

    # Merging all arrays
    ############################################################################
    Combined_Global_Array = []
    temp_count = 0
    # for array_values in Global_Array_Of_Data:
    #     #dynamic_temp_object[cols]= np.concatenate data[columns[temp_count]].tolist()
    #     print("Concatenated Arrays are ==> " + " Col No. " + str(temp_count) + " ==> ")
    #     print(Global_Array_Of_Data[temp_count])

    #     # list out keys and values separately
    #     key_list_Global_Array = list(Global_Array_Of_Data.keys())
    #     val_list_Global_Array = list(Global_Array_Of_Data.values())

    #     key_list_Column_Array = list(TempColumns.keys())
    #     val_list_Column_Array = list(TempColumns.values())

    #     for column_names in TempColumns:
    #         # print key with val Current Column name
    #         position = val_list_Column_Array.index(column_names)
    #         print(key_list_Column_Array[position])
    #         if()
    #     temp_count = temp_count + 1
    #print("Global Array of Data is ==> ",Global_Array_Of_Data)
    ############################################################################
    ##Final merging"""@Algorithm
    ############################################################################
    # 
    # 
    for column_sheet in TempColumns:
        temp_count_of_global_array=0

        final_dynamic_temp_object = {}

        for global_array_data in Global_Array_Of_Data:
            #### list out keys and values separately ####
            key_list = list(Global_Array_Of_Data[temp_count_of_global_array].keys())
            val_list = list(Global_Array_Of_Data[temp_count_of_global_array].values())
            # print key with val 100
            position = key_list.index(column_sheet)
            
            #print(key_list[position])
            #### list out keys and values separately ####
            if(key_list[position]==column_sheet):
                print(key_list[position])
                final_dynamic_temp_object[key_list[position]]=data[columns[temp_count_of_global_array]].tolist()

                Combined_Global_Array.append(final_dynamic_temp_object)    
              
            temp_count_of_global_array=temp_count_of_global_array+1  
    # Greater_Longitude_Combined = np.concatenate((Greater_Longitude))
    # Greater_Latitude_Combined = np.concatenate((Greater_Latitude))
    # Greater_Date_Combined = np.concatenate((Greater_Date))
    # Greater_NDVI_Combined = np.concatenate((Greater_NDVI))
    # Greater_Product_Combined = np.concatenate((Greater_Product))

    #print("Combined Global Array of data ==> ",Combined_Global_Array)

    # counter = 0
    # print("Type is : "+str(type(Combined_Global_Array)))
    # for val in Combined_Global_Array:
    #     print(val)
    #     counter = counter + 1
    #     if(counter == 2):
    #         break
    
    ####################################################################
    #Merging Similar keys of dictionaries in same output from Combined Global Array object
    #s = [{'Input.txt': 'Randy'}, {'Input.txt': 'Stan'}, {'Output.txt': 'Randy'}]
    dictionary=merge_list_of_dictionaries(Combined_Global_Array)
  
    # dictlist=[]

    # for key, value in dictionary.items():
    #     temp = [key,value]
    #     dictlist.append(temp)

    #print(dictionary)

    # split dictionary into keys and values
    NewListOfDict = []
    items = dictionary.items()
    for item in items:
        NewListOfDict.append({item[0]:item[1]})
  
    # printing keys and values separately
    #print ("New List of Dictionary : ", NewListOfDict)
    ####################################################################Finally Writing Data
    # temp_final_count = 0
    # #This final dict will be wrote to the csv
    # finalObjToBeWrote = {}
    # for col_names in TempColumns:   
    #     temp_count_of_NewList_Dict=0 
    #     for combined_array in Combined_Global_Array:
    #         #Getting the keys separate out of list of objects to check for the condition
    #         key_list = list(Combined_Global_Array[temp_count_of_NewList_Dict].keys())
    #         val_list = list(Combined_Global_Array[temp_count_of_NewList_Dict].values())
    #         # print key with val 100
    #         position = key_list.index(col_names)
    #         #print(position)
    #         print(key_list[position])
    #         #### list out keys and values separately ####
    #         if(col_names == key_list[position]):
    #             print(col_names)
    #         #if(col_names == key_list[position]):
    #         #     #print(combined_array)
    #         #     finalObjToBeWrote[col_names] = "bilal"
    #         temp_final_count = temp_final_count + 1



    for column_sheet in TempColumns:
        temp_count_of_global_array=0

        final_dynamic_temp_object = {}

        for global_array_data in NewListOfDict:
            #### list out keys and values separately ####
            #key_list = list(NewListOfDict[temp_count_of_global_array].keys())
            #val_list = list(NewListOfDict[temp_count_of_global_array].values())
            # print key with val 100
            #position = key_list.index(column_sheet)
            
            #print(key_list[position])
            #### list out keys and values separately ####
            #if(key_list[position]==column_sheet):
                pass
                #print(key_list[position])
                # final_dynamic_temp_object[key_list[position]]=data[columns[temp_count_of_global_array]].tolist()
 
                # Combined_Global_Array.append(final_dynamic_temp_object)    
              
            #temp_count_of_global_array=temp_count_of_global_array+1  
    
    ####################################################################Finally Writing Data

    count = 0
    for check in NewListOfDict:
        print(check)
        #print(count)
        count = count + 1 
    print(count)

    #Getting the keys separate out of list of objects to check for the condition
    finalObjToBeWrote = {}

    for col_names in TempColumns:
        finalObjToBeWrote[col_names]=[]
    
    # l = "longitude"
    # key_list = list(NewListOfDict[0].keys())
    # val_list = list(NewListOfDict[0].values())
    # finalObjToBeWrote[key_list[0]] = val_list[0]
    print(finalObjToBeWrote)

    count = 0
    for col_names in TempColumns:
        temp_count_of_global_array=0

        key_list = list(NewListOfDict[count].keys())
        val_list = list(NewListOfDict[count].values())
        count = count + 1
        #print(key_list[0])
        for list_new in NewListOfDict:
            if(col_names==key_list[0]):
                #print(key_list[0])
                finalObjToBeWrote[key_list[0]]=val_list[0]
                #print(col_names)
                pass
            temp_count_of_global_array = temp_count_of_global_array + 1
            #print(finalObjToBeWrote)

    # val_list = list(Combined_Global_Array[temp_count_of_NewList_Dict].values())
    # print key with val 100
    #position = key_list.index(col_names)
    #print(position)
    print(finalObjToBeWrote)


    # printing list data
    # print('Length of longitude Array is : ', len(Greater_Longitude_Combined))
    # print('Length of latitude Array is : ', len(Greater_Latitude_Combined))
    # print('Length of date Array is :', len(Greater_Date_Combined))
    # print('Length of NDVI Array is :', len(Greater_NDVI_Combined))
    # print('Length of product Array is :', len(Greater_Product_Combined))

    # Printing finally as arrays
    # print('longitude Array is : ', Greater_Longitude_Combined)
    # print('latitude Array is : ', Greater_Latitude_Combined)
    # print('date Array is :', Greater_Date_Combined)
    # print('NDVI Array is :', Greater_NDVI_Combined)
    # print('product Array is :', Greater_Product_Combined)

    # Writing data finally to csv file
    # df = pd.DataFrame(
    #     {
    #         "longitude": Greater_Longitude_Combined,
    #         "latitude": Greater_Latitude_Combined,
    #         "date": Greater_Date_Combined,
    #         "NDVI": Greater_NDVI_Combined,
    #         "product": Greater_Product_Combined
    #     }
    # )
    # df.to_csv("Test 0.csv", index=False)
    #Will be tested later
    return

def main(): 
    path = 'H:/sir zeeshan work data science/test/0/'
    merge_all_csv_in_directory(path)

main()