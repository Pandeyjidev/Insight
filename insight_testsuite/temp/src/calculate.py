from get_running_data import get_running_median
from get_running_data import get_running_median_date
from write_file import write_file_data
from write_file import write_file_data_date
from to_string import convert_to_string
from operator import itemgetter
from chron_sort import sort_chronologically
from cmte_sort import sort_by_cmte
import math
def calculate_data(data):
    medianvals_by_zip = []
    medianvals_by_date = []
    master_dict = {}
    date_dict ={}
    median_dict = {}
    for record in data:
        if master_dict.get((record[0],record[1]),None):
            zip_data = get_running_median(master_dict,record,master_dict[(record[0],record[1])],0)
            medianvals_by_zip.append([record[0],record[1],zip_data[0],zip_data[1],zip_data[2]])
            master_dict[(record[0],record[1])]= zip_data
        else:
            master_dict[(record[0],record[1])] = [int(record[3]),int(1),int(record[3])]
            medianvals_by_zip.append([record[0],record[1],int(record[3]),int(1),int(record[3])])
        if date_dict.get((record[0],record[2]),None):
            # print(median_dict[(record[0],record[2])])
            median_dict[(record[0],record[2])].append(int(record[3]))
            # print(median_dict[(record[0],record[2])])
            # old = median_dict[(record[0],record[2])]
            # newlist = []
            # for med in range(len(old)):
            #     if len(old) == 1:
            #         newlist = [old] + [record[2]]
            #     else:
            #         newlist = newlist + old[med]
            # newlist = newlist + record[3]
            # print(newlist)
            # median_dict[(record[0],record[2])] = newlist
            date_dict[(record[0],record[2])] = get_running_median_date(date_dict,record,date_dict.get((record[0],record[2]),None),1)
        else:
            median_dict[(record[0],record[2])] = [int(record[3])]
            # print(median_dict[(record[0],record[2])])
            date_dict[(record[0],record[2])] = [int(record[3]),int(1),int(record[3])]
    for record in sorted(date_dict.keys(),key=itemgetter(0)):
        key_median = median(median_dict[record])
        medianvals_by_date.append([record[0],record[1],key_median,date_dict[record][1],date_dict[record][2]])
    # Sort Chronologically here
    # medianvals_by_date = sort_chronologically(medianvals_by_date)
    medianvals_by_date_str = convert_to_string(medianvals_by_date)
    medianvals_by_zip_str = convert_to_string(medianvals_by_zip)
    write_file_data_date(medianvals_by_date_str,"medianvals_by_date.txt")
    write_file_data(medianvals_by_zip_str,"medianvals_by_zip.txt")
    return master_dict

def median(lst):
    
    lst.sort()
    a = len(lst)
    if a % 2 == 0:
        b = float(lst[len(lst)/2])
        c = float(lst[(len(lst)/2)-1])
        d = float((b+c) / 2)
        e = int((int(b)+int(c) )/ 2)
        if(d-float(e)>=0.5):
            e = int(math.ceil(d))
        else:
            e = int(math.floor(d))
        return e
    if a % 2 > 0:
        
        return lst[len(lst)/2]
        
