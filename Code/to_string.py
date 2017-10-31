def convert_to_string(array):
    new_array = ""
    for row in array:
        new_array = new_array + row[0] + "|" + row[1] + "|" + str(row[2]) + "|" + str(row[3]) + "|" + str(row[4]) + "\n"
    # print(new_array)
    return new_array


