import io

def clean_data_for_processing(filename,delimiter):
    data_list = []
    with io.open(filename, 'r') as file:
        for line in file:
            list_of_values = line.split(delimiter)
            list_of_values = get_relevant_data(list_of_values)
            data_list = data_list + [list_of_values]
    return data_list
# Filter important columns
def get_relevant_data(list_of_values):
    list_of_values = list_of_values + ["|","|","|","|","|","|","|","|","|","|","|","|","|","|","|","|","|","|","|","|","|",]
    return [str(list_of_values[0]),str(list_of_values[10]),str(list_of_values[13]),str(list_of_values[14]),str(list_of_values[15])]
