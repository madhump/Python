import numbers


def findnumbers(arraylist, number):

 try:
    num_index = arraylist.index(number)
    return str("Record found at ") + num_index
 except:
    return str("Not found")

#---------------------------------------------------

Input_1 = input("Enter the Array value1")
Input_2 = input("Enter the Array value2")
Input_3 = input("Enter the Array value3")
Input_4 = input("Enter the Array value4")

final_array = [Input_1, Input_2, Input_3, Input_4]

Number_to_search = input("Enter the number to search in Array \n")

Number_results = findnumbers(final_array, Number_to_search)

print("Number Result " + str(Number_results))
