# Stream input and send for processing
import io
import os
from filelist import get_filelist
def runner():
    cwd = os.path.dirname(os.path.realpath(__file__))
    filelist = get_filelist()
    print(filelist)
    for file in filelist:
        file_path = os.path.join(cwd,'..','Input',file)
        import_dict = read_file(file_path)
def remove_last(element):
    return element < 6

def read_file(filename):
    import_dict = {}
    with io.open(filename, 'r') as file:
        for line in file:
            # print(line)
            list_of_values = line.split('|')
            # print(list_of_values)
            #df[x[0]] = x[1:]
            len(list_of_values)
            list_of_values = [value for value in list_of_values if value == list_of_values[0] or value == list_of_values[10] or value == list_of_values[13] or value == list_of_values[14] or value == list_of_values[15] ]
            filter(remove_last, list_of_values)
            # list_of_values = remove_values_from_list(list_of_values)
            print(list_of_values)
            # if(df[x[0]] in import_dict.keys()):
            #     #running average
            # else:
            #     import_dict[x[0]] = list_of_values
                #add to dictionary
    return list_of_values

            
if __name__ == '__main__':
    runner()