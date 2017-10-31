def get_running_median(main_list, record, zip_or_date,zip_or_date_num):
    old_median = int(zip_or_date[0])
    curr_median = int(record[3])
    if zip_or_date_num == 0:
        Number_of_transaction = int(zip_or_date[zip_or_date_num+1])
    else:
        Number_of_transaction = int(zip_or_date[zip_or_date_num])
    Number_of_transaction = Number_of_transaction + 1
    total_amount = old_median+curr_median
    new_median = (total_amount)/Number_of_transaction
    return [new_median,Number_of_transaction,total_amount]