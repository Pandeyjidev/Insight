from get_running_data import get_running_median
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
            zip_data = get_running_median(master_dict,record,master_dict.get((record[0],record[1]),None),0)
            print(zip_data)
            medianvals_by_zip.append([record[0],record[1],zip_data[0],zip_data[1],zip_data[2]])
            master_dict[(record[0],record[1])]= zip_data
        else:
            # print("in ZIP else")
            data_and_zip_dict = {}
            # data_and_zip_dict[record[1]] = [[int(record[3]),int(1),int(record[3])]]
            master_dict[(record[0],record[1])] = [int(record[3]),int(1),int(record[3])]
            medianvals_by_zip.append([record[0],record[1],int(record[3]),int(1),int(record[3])])
        if master_dict.get((record[0],record[2]),None):
            # print("in T_DT")
            date_data = get_running_median(master_dict,record,master_dict.get((record[0],record[2]),None),1)
            medianvals_by_date.append([record[0],record[2],date_data[0],date_data[1],date_data[2]])
            master_dict[(record[0],record[2])] = date_data
        else:
            # print("in T_DT else")
            medianvals_by_date.append([record[0],record[2],int(record[3]),int(1),int(record[3])])
            master_dict[(record[0],record[2])] = [int(record[3]),int(1),int(record[3])]
        # else:
        #     print("in CMTE_ID else")
        #     medianvals_by_zip.append([record[0],record[1],int(record[3]),int(1),int(record[3])])
        #     medianvals_by_date.append([record[0],record[2],int(record[3]),int(1),int(record[3])])
        #     # dictionary
        #     master_dict[(record[0],record[2])] = [int(record[3]),int(1),int(record[3])]
        #     master_dict[(record[0],record[1])] = [int(record[3]),int(1),int(record[3])]
        #     print(master_dict[(record[0],record[1])])
        #     # print(ZIP_CODE)
    for zip_rec in medianvals_by_zip:
        print(zip_rec)
    print('\n')
    print('\n')
    for date_rec in medianvals_by_date:
        print(date_rec)
    # for record in master_dict:
        # print(record)
    return data


        
