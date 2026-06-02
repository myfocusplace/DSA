# Credited to https://www.interviewcake.com/concept/python3/heapsort


def left_child_index(parent_index):
    return parent_index * 2 + 1


def right_child_index(parent_index):
    return parent_index * 2 + 2


def bubble_down(heap, heap_length, index):
    while index < heap_length:
        left_index = left_child_index(index)
        right_index = right_child_index(index)

        #There is no more children to compare with
        if left_index >= heap_length:
            break

        larger_child_index = left_index
        if right_index < heap_length and heap[right_index] > heap[left_index]:
            larger_child_index = right_index

        if heap[index] < heap[larger_child_index]:
            # Swap if the larger child element is indeed greater than the current
            heap[index], heap[larger_child_index] = (
                heap[larger_child_index],
                heap[index],
            )
            index = larger_child_index  # Continue to check the rest of the children
        else:
            break


def remove_max(heap, heap_length):
    max_value = heap[0]
    heap[0] = heap[heap_length - 1]
    bubble_down(heap, heap_length - 1, 0)
    return max_value


def heapify(the_list):
    for index in range(len(the_list) - 1, -1, -1):
        bubble_down(the_list, len(the_list), index)


"""
heapify:     every node might be out of place → fix ALL of them
             bubble_down(... index 5)
             bubble_down(... index 4)
             bubble_down(... index 3)
             ...

remove_max:  only the ROOT is out of place → fix just that one
             bubble_down(... index 0)  ← always the root
"""
