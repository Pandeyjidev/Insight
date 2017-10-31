import math
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
    f_new_median = float((float(total_amount)/float(Number_of_transaction)))
    if f_new_median-float(new_median)>=0.5:
        new_median = int(math.ceil(f_new_median))
    else:
        new_median = int(math.floor(f_new_median))
    return [new_median,Number_of_transaction,total_amount]

def get_running_median_date(main_list, record, date,date_num):
    old_median = int(date[0])
    curr_median = int(record[3])
    total_amount = int(date[2])
    Number_of_transaction = int(date[date_num])
    Number_of_transaction = Number_of_transaction + 1
    total_amount = total_amount + curr_median
    new_median = (total_amount)/Number_of_transaction
    f_new_median = float((float(total_amount)/float(Number_of_transaction)))
    if f_new_median-float(new_median)>=0.5:
        new_median = int(math.ceil(f_new_median))
    else:
        new_median = int(math.floor(f_new_median))
    return [new_median,Number_of_transaction,total_amount]