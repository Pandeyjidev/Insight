import os.path
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
