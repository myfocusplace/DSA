from utils.util import negate_all
from sorting.selection_sort import selection_sort

def main():
    array = [1, 2, 3, 4, 5]
    negated = negate_all(array)
    print(negated)

    array = [5, 1, 3, 4, 2]
    selection_sort_array = selection_sort(array)
    print(selection_sort_array)


if __name__ == "__main__":
    main()