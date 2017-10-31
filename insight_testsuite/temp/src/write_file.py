import os.path
from to_string import convert_to_string
def write_file_data(array,thefile):
    done = "Operation successfully completed"
    os.chdir("../output/")
    cwd = os.getcwd()
    complete_path = os.path.join(cwd, thefile)
    with open(complete_path, 'a') as f:
        for line in array:
            f.write(str(line))
    f.close()
    print done
def write_file_data_date(array,thefile):
    done = "Operation successfully completed"
    os.chdir("../output/")
    cwd = os.getcwd()
    complete_path = os.path.join(cwd, thefile)
    with open(complete_path, 'w') as f:
        # for line in array:
            # line2 = str(convert_to_string(line))
        f.write(array)
    
    f.close()
    print done
