def convert_to_string(array):
    new_array = ""
    counter = 0
    for row in array:
        if(counter < len(array)-1):
            new_array = new_array + row[0] + "|" + row[1] + "|" + str(row[2]) + "|" + str(row[3]) + "|" + str(row[4]) + "\n"
        else:
            new_array = new_array + row[0] + "|" + row[1] + "|" + str(row[2]) + "|" + str(row[3]) + "|" + str(row[4])
        counter +=1
    return new_array


