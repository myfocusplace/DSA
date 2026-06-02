def insertion_sort(the_list):
    for index in range(len(the_list)):
        while index > 0 and the_list[index-1] >= the_list[index]:
            the_list[index-1], the_list[index] = the_list[index], the_list[index-1]
            index -= 1
    return the_list