# d_input = {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}
# res = {}
# for i, v in d_input.items():
#     res[v] = [i] if v not in res.keys() else res[v] + [i]
# print(res)

#Suno mere pass list of objects hai ab us ke hisab se dekhna hai 
# is tarah

# [ { key:val },{ key:val },{ key:val } ]

# def grouping_dictionary(l):
#     result = {}
#     for k, v in l:
#          result.setdefault(k, []).append(v)
#     return result
# colors = [{'Input.txt': 'Randy'}, {'Code.py': 'Stan'}, {'Output.txt': 'Randy'}]
# print("Original list:")
# print(colors)
# print("\nGrouping a sequence of key-value pairs into a dictionary of lists:")
# print(grouping_dictionary(colors))

def merge_list_of_dictionaries(dict_list):
  new_dict = {}
  for d in dict_list:
    for d_key in d:
      if d_key not in new_dict:
        new_dict[d_key] = []
      new_dict[d_key].append(d[d_key])
  return new_dict

def main():
    s = [{'Input.txt': 'Randy'}, {'Input.txt': 'Stan'}, {'Output.txt': 'Randy'}]
    dictionary=merge_list_of_dictionaries(s)
  
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
    print ("New List of Dictionary : ", NewListOfDict)

    # for i in dictionary:
    #     print(i)

main()