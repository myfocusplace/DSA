# Given an array, sales, find the most sales in any 7-day period
# sales = [0, 3, 7, 12, 10, 5, 0, 1, 0, 15, 12, 11, 1]
# output = 44
def most_weekly_sales(sales):
    l, r = 0, 0
    curr_max = 0
    curr_window_sum = 0

    while r < len(sales):
        curr_window_sum += sales[r]
        r += 1
        if r - l == 7:
            curr_max = max(curr_max, curr_window_sum)
            curr_window_sum -= sales[l]
            l += 1

    return curr_max


# Given the array sales and a number k with 1 <= k <= len(sales), find
# the most sales in any k-day period.
# Return the first day of the k-day period with the most sales.
# [8, 1, 3, 7]
# Given the array sales and a number k with 1 <= k <= len(sales), find
# the most sales in any k-day period.
# Return the first day of the k-day period with the most sales.
# [8, 1, 3, 7]
# k = 2
def most_sales_k_days(sales, k):
    l, r = 0, 0
    curr_window_sum = 0
    best_sum = 0
    best_index = 0
    while r < len(sales):
        curr_window_sum += sales[r]
        r += 1
        if r - l == k:
            if curr_window_sum > best_sum:
                best_sum = curr_window_sum
                best_index = l
            curr_window_sum -= sales[l]
            l += 1
    return best_index


def alternate_most_sales_k_days_solution(sales, k):
    # Build the first window
    window_sum = sum(sales[:k])
    best_sum = window_sum
    best_index = 0

    # Slide the window one day at a time
    for l in range(1, len(sales) - k + 1):
        window_sum += sales[l + k - 1] - sales[l - 1]
        if window_sum > best_sum:
            best_sum = window_sum
            best_index = l

    return best_index


# Given the array best_seller and a number k with 1 <= k < = len(best_seller)
# return whether there is any k-day period where each day has a different best-selling title.
# best_seller = ["book3", "book1", "book3", "book3", "book2", "book3", "book4", "book3"]
# k = 3
# Output = True. There is a 3-day period without a repeated value: ["book2", "book3", "book4"]
def no_repeat_value(best_seller, k):
    for l in range(1, len(best_seller) - k + 1):
        window = best_seller[l : l + k]
        if len(set(window)) == k:  # all k items are unique
            return True
    return False


# Given the array best_seller and a number k with 1 <= k <= len(best_seller), return whether there
# is any k-day period where every day has the same best selling title
# best_seller = ["book3", "book1", "book3", "book3", "book2"]
# k = 3
def everyday_same_title(best_seller, k):
    for l in range(1, len(best_seller) - k + 1):
        window = best_seller[l : l + k]
        if len(set(window)) == 1:
            return True
    return False
