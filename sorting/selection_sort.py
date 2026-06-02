"""
Select the smallest element from an unsorted list and
move it to the front
Space efficient algorithm but slow as it takes O(n^2) time
Credit to https://www.interviewcake.com/concept/python3/selection-sort
"""

def selection_sort(the_list):
    for i in range(len(the_list)):
        smallest_index = i
        for j in range(i + 1, len(the_list)):
            if the_list[j] < the_list[smallest_index]:
                smallest_index = j

        #swap the first selected element with the smallest element
        the_list[i], the_list[smallest_index] = (
            the_list[smallest_index],
            the_list[i],
        )
    return the_list