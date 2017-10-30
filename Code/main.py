# Stream input and send for processing
import io
import os
from filelist import get_filelist
from process import process_data
def runner():
    cwd = os.path.dirname(os.path.realpath(__file__))
    filelist = get_filelist()
    print(filelist)
    for file in filelist:
        file_path = os.path.join(cwd,'..','Input',file)
        clean_data = clean_data_for_processing(file_path)
        processed_data = process_data(clean_data)
        print(processed_data)
def get_relevant_data(list_of_values):
    return [str(list_of_values[0]),str(list_of_values[10]),str(list_of_values[13]),str(list_of_values[14]),str(list_of_values[15])] 

def clean_data_for_processing(filename):
    data_list = []
    with io.open(filename, 'r') as file:
        for line in file:
            list_of_values = line.split('|')
            list_of_values = get_relevant_data(list_of_values)
            data_list = data_list + [list_of_values]
    return data_list

            
if __name__ == '__main__':
    runner()