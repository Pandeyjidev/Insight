def get_running_median(main_list, record, zip_or_date,zip_or_date_num):
    # print(zip_or_date)
    # print("in run")
    old_median = int(zip_or_date[0])
    curr_median = int(record[3])
    # print(old_median)
    # print(curr_median)
    # print("++++++")
    # print(zip_or_date)
    print("++++++")
    Number_of_transaction = int(zip_or_date[zip_or_date_num])
    Number_of_transaction = Number_of_transaction + 1
    print(Number_of_transaction)
    total_amount = old_median+curr_median
    print(total_amount)
    new_median = (total_amount)/Number_of_transaction
    print(new_median)
    print([new_median,Number_of_transaction,total_amount])
    print("++++++")
    print("before return")
    return [new_median,Number_of_transaction,total_amount]