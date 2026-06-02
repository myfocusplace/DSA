from data_structure.heap import heapify, remove_max

'''
Turn the array into a max-heap with heapify
Then use remove_max to repeatedly take out the largest
element and put it at the end of the array

Inside remove_max it automatically bubble_down for you already
'''
def heap_sort(the_list):
    heapify(the_list)
    heap_size = len(the_list)
    while heap_size > 0:
        largest_value = remove_max(the_list, heap_size)
        heap_size -= 1
        the_list[heap_size] = largest_value
