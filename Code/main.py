# Stream input and send for processing
import os
from filelist import get_filelist
from clean import clean_data_for_processing
from process import process_data
from calculate import calculate_data
from print_data import print_list
def runner(delimiter):    
    cwd = os.path.dirname(os.path.realpath(__file__))
    filelist = get_filelist()
    for file in filelist:
        file_path = os.path.join(cwd,'..','Input',file)
        # Clean data
        clean_data = clean_data_for_processing(file_path,delimiter)
        # Process data
        processed_data = process_data(clean_data)
        # Calculate and Restructure data
        calculated_data = calculate_data(processed_data)
        # print_list(calculated_data)
          
if __name__ == '__main__':
    delimiter = '|'
    runner(delimiter)