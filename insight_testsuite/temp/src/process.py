import copy
def process_data(data):
    constructing_data = []
    for record in data:
        if '' == record[4] and '' != record[0] and '' != record[3]:
            record[1] = record[1][:5]
            constructing_data.append(record)
    # print_list(constructing_data)
    return constructing_data
# for testing
def print_list(processed_list):
    for record in processed_list:
        print(record)
    print("\n")