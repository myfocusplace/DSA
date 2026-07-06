# Given an array, sales, find the most consecutive days with no bad days (fewer than 10 sales)
# Example: sales = [0, 14, 7, 12, 10, 20]
# Output: 3 [12, 10, 20] has no bad days
def most_consecutive_good_days(sales):
    l, r = 0, 0
    longest_good_days = 0
    while r < len(sales):
        if sales[r] > 9:
            longest_good_days = max(longest_good_days, (r - l + 1))
            r += 1
        else:
            l = r + 1
            r += 1
    return longest_good_days


def most_consecutive_good_days_alternate(sales):
    l = 0
    longest_good_days = 0
    for r in range(len(sales)):
        if sales[r] > 9:
            longest_good_days = max(longest_good_days, r - l + 1)
        else:
            l = r + 1
    return longest_good_days
