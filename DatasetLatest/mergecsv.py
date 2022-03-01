# Converting to package
def merge_csv(path_):
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

    #print("Files and directories in '", path, "' :")

    # Length of directory
    print("Length of files in the given path directory is : " + str(len(dir_list)))
    length = len(dir_list)

    # Greater loop to go through each file name
    count = 0
    Greater_Longitude = []
    Greater_Latitude = []
    Greater_NDVI = []
    Greater_Max_Temp = []
    Greater_Ave_Temp = []
    Greater_Min_Temp = []
    Greater_Ave_Humidity = []
    Greater_Rainfall = []
    Greater_Crop_Type = []

    # We are inside the loop.Get ready the loop is going to start
    for files in dir_list:
        # print(files)
        # Path Format: H:/sir zeeshan work/train/0/
        # H:/sir zeeshan work/val/0/
        # H:/sir zeeshan work/Coding files/Val/
        data = pd.read_csv(path_ +
                           str(files))
        print(files)

        longitude = data['longitude'].tolist()
        latitude = data['latitude'].tolist()
        ndvi = data['NDVI'].tolist()
        max_temp = data['Max Temp'].tolist()
        ave_temp = data['Ave Temp'].tolist()
        min_temp = data['Min Temp'].tolist()
        ave_humidity = data['Ave Humidity'].tolist()
        rainfall = data['Rainfall'].tolist()
        crop_type = data['Crop_Type'].tolist()
        #########################APPENDING THE DATA#######################################
        Greater_Longitude.append(longitude)
        Greater_Latitude.append(latitude)
        Greater_NDVI.append(ndvi)
        Greater_Max_Temp.append(max_temp)
        Greater_Ave_Temp.append(ave_temp)
        Greater_Min_Temp.append(min_temp)
        Greater_Ave_Humidity.append(ave_humidity)
        Greater_Rainfall.append(rainfall)
        Greater_Crop_Type.append(crop_type)

        # Printing the count to know at which length the memory leak is occuring
        #print("Count =====================> ",count)

        # Breaking the loop to avoid memory leak when the files length available in the folder or directory are reached.Discovered to avoid memory leak
        count = count + 1
        if(count == length-1):
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

#   Greater_Longitude.append(longitude)
#         Greater_Latitude.append(latitude)
#         Greater_NDVI.append(ndvi)
#         Greater_Max_Temp.append(max_temp)
#         Greater_Ave_Temp.append(ave_temp)
#         Greater_Min_Temp.append(min_temp)
#         Greater_Ave_Humidity.append(ave_humidity)
#         Greater_Rainfall.append(rainfall)
#         Greater_Crop_Type.append(crop_type)

    Greater_Longitude_Combined = np.concatenate((Greater_Longitude))
    Greater_Latitude_Combined = np.concatenate((Greater_Latitude))
    Greater_NDVI_Combined = np.concatenate((Greater_NDVI))
    Greater_Max_Temp_Combined = np.concatenate((Greater_Max_Temp))
    Greater_Ave_Temp_Combined = np.concatenate((Greater_Ave_Temp))
    Greater_Min_Temp_Combined = np.concatenate((Greater_Min_Temp))
    Greater_Ave_Humidity_Combined = np.concatenate((Greater_Ave_Humidity))
    Greater_Rainfall_Combined = np.concatenate((Greater_Rainfall))
    Greater_Crop_Type_Combined = np.concatenate((Greater_Crop_Type))

    # printing list data
    print('Length of longitude Array is : ', len(Greater_Longitude_Combined))
    print('Length of latitude Array is : ', len(Greater_Latitude_Combined))
    print('Length of NDVI Array is :', len(Greater_NDVI_Combined))
    print('Length of Max Temp Array is :', len(Greater_Max_Temp))
    print('Length of Ave Temp Array is :', len(Greater_Ave_Temp))
    print('Length of Min Temp Array is :', len(Greater_Min_Temp))
    print('Length of Ave Humidity Temp Array is :', len(Greater_Ave_Humidity))
    print('Length of rainfall Array is :', len(Greater_Rainfall))
    print('Length of Crop Type Array is :', len(Greater_Crop_Type))

    # Printing finally as arrays
    print('longitude Array is : ', Greater_Longitude_Combined)
    print('latitude Array is : ', Greater_Latitude_Combined)
    print('NDVI Array is :', Greater_NDVI_Combined)
    print('Max Temp Array is :', Greater_Max_Temp_Combined)
    print('Ave Temp Array is :', Greater_Ave_Temp_Combined)
    print('Min Temp Array is :', Greater_Min_Temp_Combined)
    print('Ave Humidity Array is :', Greater_Ave_Humidity_Combined)
    print('Rainfall Array is :', Greater_Rainfall_Combined)
    print('Crop Type Array is :', Greater_Crop_Type_Combined)

    # Writing data finally to csv file
    df = pd.DataFrame(
        {
            "longitude": Greater_Longitude_Combined,
            "latitude": Greater_Latitude_Combined,
            "NDVI": Greater_NDVI_Combined,
            "Max Temp": Greater_Max_Temp_Combined,
            "Ave Temp": Greater_Ave_Temp_Combined,
            "Min Temp": Greater_Min_Temp_Combined,
            "Ave Humidity": Greater_Ave_Humidity_Combined,
            "Rainfall":Greater_Rainfall_Combined,
            "Crop_Type":Greater_Crop_Type_Combined
        }
    )
    df.to_csv("Combined.csv", index=False)
    return

def main():
    path = 'H:/sir zeeshan work data science/DatasetLatest/'
    merge_csv(path)

main()
