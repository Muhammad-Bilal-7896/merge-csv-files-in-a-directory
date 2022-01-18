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
        if(count == 5):
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
    # temp_count = 0
    # for cols in TempColumns:
    #     dynamic_temp_object[cols]=data[columns[temp_count]].tolist()
    #     temp_count = temp_count + 1
    print("Global Array of Data is ==> ",Global_Array_Of_Data)
    ############################################################################
    # Greater_Longitude_Combined = np.concatenate((Greater_Longitude))
    # Greater_Latitude_Combined = np.concatenate((Greater_Latitude))
    # Greater_Date_Combined = np.concatenate((Greater_Date))
    # Greater_NDVI_Combined = np.concatenate((Greater_NDVI))
    # Greater_Product_Combined = np.concatenate((Greater_Product))

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