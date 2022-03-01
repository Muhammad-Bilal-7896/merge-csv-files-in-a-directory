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
    # Lets make its creation dynamic
    # Greater_Longitude = []
    # Greater_Latitude = []
    # Greater_Date = []
    # Greater_NDVI = []
    # Greater_Product = []
    # Lets make its creation dynamic

    TempCheck = pd.read_csv(path_ +
                            str(dir_list[0]))

    TempColumns = list(TempCheck.head(0))

    length_of_csv_headers = len(TempColumns)

    #print("Reading csv we got ==> ",length_of_csv_headers)

    Global_Array_Of_Data = []

    # Pushing empty arrays
    # for col_names in TempColumns:
    #     print(col_names)
    #     Global_Array_Of_Data.append({ col_names: [] })

    print(Global_Array_Of_Data)

    # Will be tested later
    # We are inside the loop.Get ready the loop is going to start
    for files in dir_list:
        # print(files)
        # Path Format: H:/sir zeeshan work/train/0/
        # H:/sir zeeshan work/val/0/
        # H:/sir zeeshan work/Coding files/Val/
        data = pd.read_csv(path_ +
                           str(files))

        # Reading Column Names
        columns = list(data.head(0))

        # Focus here later
        # print("The column names are : ",columns)

        # longitude = data[columns[0]].tolist()
        # latitude = data[columns[1]].tolist()
        # date = data[columns[2]].tolist()
        # NDVI = data[columns[3]].tolist()
        # product = data[columns[4]].tolist()

        dynamic_temp_object = {}

        temp_count = 0
        for cols in TempColumns:
            dynamic_temp_object[cols] = ["data[columns[temp_count]].tolist()","sdafa"]
            temp_count = temp_count + 1
            # print("Value ===> ",temp_count)

        #print("T is ==> ",dynamic_temp_object)

        # Pushing the object in global array after filling it with appropriate key and values
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
        if(count == length-1):
            break
    # The loop Ended Successfully.Done

    print(Global_Array_Of_Data)
    
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

    ############################################################################
    # Final merging"""@Algorithm
    ############################################################################
    #
    #
    for column_sheet in TempColumns:
        temp_count_of_global_array = 0

        final_dynamic_temp_object = {}

        for global_array_data in Global_Array_Of_Data:
            #### list out keys and values separately ####
            key_list = list(
                Global_Array_Of_Data[temp_count_of_global_array].keys())
            val_list = list(
                Global_Array_Of_Data[temp_count_of_global_array].values())
            # print key with val 100
            position = key_list.index(column_sheet)

            # print(key_list[position])
            #### list out keys and values separately ####
            if(key_list[position] == column_sheet):
                print(key_list[position])
                final_dynamic_temp_object[key_list[position]] = data[columns[temp_count_of_global_array]].tolist()
###########IDHAR GHOR KARIN
                Combined_Global_Array.append(final_dynamic_temp_object)

            temp_count_of_global_array = temp_count_of_global_array+1

    ####################################################################
    # Merging Similar keys of dictionaries in same output from Combined Global Array object
    #s = [{'Input.txt': 'Randy'}, {'Input.txt': 'Stan'}, {'Output.txt': 'Randy'}]
    dictionary = merge_list_of_dictionaries(Combined_Global_Array)

    # split dictionary into keys and values and Append in NewListDict
    NewListOfDict = []
    items = dictionary.items()
    for item in items:
        NewListOfDict.append({item[0]: item[1]})

    # Getting the keys separate out of list of objects to check for the condition
    finalObjToBeWrote = {}
    #Initializing the finalObjToBeWrote with keys
    for col_names in TempColumns:
        finalObjToBeWrote[col_names] = []

    #Appending the correct data i.e Arrays in finalObjToBeWrote dict
    count = 0
    for col_names in TempColumns:
        temp_count_of_global_array = 0

        key_list = list(NewListOfDict[count].keys())
        val_list = list(NewListOfDict[count].values())
        count = count + 1
        # print(key_list[0])
        for list_new in NewListOfDict:
            if(col_names == key_list[0]):
                # print(key_list[0])
                arr = np.concatenate(val_list[0])
                # print(arr)
                finalObjToBeWrote[key_list[0]] = arr
                # print(col_names)
            temp_count_of_global_array = temp_count_of_global_array + 1
            # print(finalObjToBeWrote)
    #Appending the correct data i.e Arrays in finalObjToBeWrote dict
    # print(NewListOfDict)

    #Finally Concatenating the Seprate arrays into one and storing with respect to its keys
    merged_final_array = {}
    count = 0
    for list_new in NewListOfDict:
        # print("==========================>")
        key_list = list(NewListOfDict[count].keys())
        val_list = list(NewListOfDict[count].values())
        merge_them = np.concatenate(val_list[0])
        merged_final_array[key_list[0]] = merge_them
        # print(merge_them)
        count = count + 1

    print(merged_final_array)
    #Finally Concatenating the Seprate arrays into one and storing with respect to its keys

    # Finally Writing data finally to csv file
    df = pd.DataFrame(merged_final_array)
    df.to_csv("FinalMergedFile.csv", index=False)
    # Finally Writing data finally to csv file
    return

def main():
    path = 'H:/sir zeeshan work data science/test/0/'
    merge_all_csv_in_directory(path)

main()
