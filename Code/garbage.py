def remove_values_from_list(the_list):
    filter(remove_last, the_list)
    the_list(filter(lambda x:[1,2,3,4,5,6,7,8,9,11,12],the_list))
    
    # filter((val for num in range(1,10)),the_list)
    # print(the_list)
    # for value in [1,2,3,4,5,6,7,8,9,11,12]:
    #     the_list.remove(the_list(value))
    return the_list