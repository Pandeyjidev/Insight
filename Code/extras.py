from get_running_data import get_running_median
# C00177436|30004|384|1|384
# C00384818|02895|250|1|250
# C00177436|30750|230|1|230
# C00177436|04105|384|1|384
# C00384818|02895|292|2|583
# C00177436|04105|384|2|768
# CMTE_ID, ZIP_CODE , Running Median, Total record count , total contribution
def calculate_data(data):
    # print(data)30004
    master_dict = {}
    medianvals_by_zip = []
    medianvals_by_date = []
    for record in data:
        
        CMTE_ID = master_dict.get(record[0],None)
        if CMTE_ID:
            # if in dictionary then find running median
            ZIP_CODE = master_dict[record[0]].get(record[1],None)
            TRANSACTION_DT = master_dict[record[0]].get(record[2],None)
            # print(ZIP_CODE)
            if ZIP_CODE:
                # print(CMTE_ID)
                zip_data = get_running_median(master_dict,record,ZIP_CODE,0)
                print(zip_data)
                # master_dict[record[0]][record[1]].append(zip_data)
                medianvals_by_zip.append(zip_data)
            else:
                data_and_zip_dict = {}
                medianvals_by_zip.append([int(record[3]),int(1),int(record[3])])
                data_and_zip_dict[record[1]] = [[int(record[3]),int(1),int(record[3])]]
                master_dict[record[0]] = data_and_zip_dict
            
            if TRANSACTION_DT:
                # print(CMTE_ID)
                date_data = get_running_median(master_dict,record,TRANSACTION_DT,1)
                # master_dict[record[0]][record[2]].append(date_value)
                medianvals_by_date.append(date_data)
            else:
                data_and_zip_dict = {}
                medianvals_by_date.append([int(record[3]),int(1),int(record[3])])
                # data_and_zip_dict[record[2]] = [[int(record[3]),int(1),int(record[3])]]
                master_dict[record[0]] = data_and_zip_dict
        else:
            data_and_zip_dict = {}
            data_and_zip_dict[record[2]] = [[int(record[3]),int(1),int(record[3])]]
            data_and_zip_dict[record[1]] = [[int(record[3]),int(1),int(record[3])]]
            master_dict[record[0]] = data_and_zip_dict
        # print(master_dict[record[0]])
        # print('\n')
        # print(master_dict[record[0]])
    # print(master_dict['C00177436'])
    # print(master_dict['C00384818'])
    return data


        
