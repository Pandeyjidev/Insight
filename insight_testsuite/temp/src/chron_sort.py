import time
from operator import itemgetter
def sort_chronologically(array):
    # print(array)
    for row in array:
        month = row[1][0:2]
        day = row[1][2:4]
        year = row[1][4:8]
        time_struct = ''.join([year,month,day])
        row.append(int(time_struct))
    for row in sorted(array,key=itemgetter(5)):
        continue
    return array