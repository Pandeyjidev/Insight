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
    for record in data:
        # print(record)
        CMTE_ID = master_dict.get(record[0],None)
        if CMTE_ID:
            # if in dictionary then find running median
            ZIP_CODE = master_dict[record[0]].get(record[1],None)
            # print(ZIP_CODE)
            if ZIP_CODE:
                # print(CMTE_ID)
                old_median = int(ZIP_CODE[-1][0])
                curr_median = int(record[3])
                Number_of_transaction = int(ZIP_CODE[-1][0])
                Number_of_transaction = Number_of_transaction + 1
                total_amount = old_median+curr_median
                new_median = (total_amount)/Number_of_transaction
                master_dict[record[0]][record[1]].append([new_median,Number_of_transaction,total_amount])
            TRANSACTION_DT = master_dict[record[0]].get(record[2],None)
            if TRANSACTION_DT:
                # print(CMTE_ID)
                old_median = int(TRANSACTION_DT[-1][0])
                curr_median = int(record[3])
                Number_of_transaction = int(TRANSACTION_DT[-1][1])
                Number_of_transaction = Number_of_transaction + 1
                total_amount = old_median+curr_median
                new_median = (total_amount)/Number_of_transaction
                master_dict[record[0]][record[2]].append([new_median,Number_of_transaction,total_amount])
                # print(master_dict[record[0]][record[1]])
                # print(new_median)
            # date_dict = {}
            # date_dict = master_dict[record[0]][0]
            # print(date_dict)
            # zip_dict = master_dict[record[0]][1]
            # print(zip_dict)
            # # if(date_dict[master_dict[record[0]][0]] != ''):
            # print("here")
            # print(date_dict)
            # zip_dict = {}
            # zip_dict = master_dict[record[0]][1]
            continue
        else:
            data_and_zip_dict = {}
            data_and_zip_dict[record[2]] = [[int(record[3]),int(1),int(record[3])]]
            data_and_zip_dict[record[1]] = [[int(record[3]),int(1),int(record[3])]]
            master_dict[record[0]] = data_and_zip_dict
        # print(master_dict[record[0]])
        # print('\n')
    print(master_dict['C00177436'])
    print(master_dict['C00384818'])
    return data

def get_running_median(main_list, curr_list, key):
    if main_list[key] and curr_list[key]:
        return
        
