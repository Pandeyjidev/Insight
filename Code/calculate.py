from get_running_data import get_running_median
from print_file import write_file_data
from to_string import convert_to_string
# C00177436|30004|384|1|384
# C00384818|02895|250|1|250
# C00177436|30750|230|1|230
# C00177436|04105|384|1|384
# C00384818|02895|292|2|583
# C00177436|04105|384|2|768
# CMTE_ID, ZIP_CODE , Running Median, Total record count , total contribution
def calculate_data(data):
    medianvals_by_zip = []
    medianvals_by_date = []
    master_dict = {}
    for record in data:
        if master_dict.get((record[0],record[1]),None):
            zip_data = get_running_median(master_dict,record,master_dict[(record[0],record[1])],0)
            medianvals_by_zip.append([record[0],record[1],zip_data[0],zip_data[1],zip_data[2]])
            master_dict[(record[0],record[1])]= zip_data
        else:
            data_and_zip_dict = {}
            master_dict[(record[0],record[1])] = [int(record[3]),int(1),int(record[3])]
            medianvals_by_zip.append([record[0],record[1],int(record[3]),int(1),int(record[3])])
        if master_dict.get((record[0],record[2]),None):
            date_data = get_running_median(master_dict,record,master_dict.get((record[0],record[2]),None),1)
            medianvals_by_date.append([record[0],record[2],date_data[0],date_data[1],date_data[2]])
            master_dict[(record[0],record[2])] = date_data
        else:
            medianvals_by_date.append([record[0],record[2],int(record[3]),int(1),int(record[3])])
            master_dict[(record[0],record[2])] = [int(record[3]),int(1),int(record[3])]
    # print(medianvals_by_date)
    # print(medianvals_by_zip)
    medianvals_by_date_str = convert_to_string(medianvals_by_date)
    medianvals_by_zip_str = convert_to_string(medianvals_by_zip)
    # print(medianvals_by_date_str)
    # print(medianvals_by_zip_str)
    write_file_data(medianvals_by_date_str,"medianvals_by_data.txt")
    write_file_data(medianvals_by_zip_str,"medianvals_by_zip.txt")
    return master_dict


        
