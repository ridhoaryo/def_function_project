def bigger_smaller(a_list):
    min_number = max(a_list)
    number_now = min(a_list)
    return (min_number, number_now)
a_list = [40, 100, 1, 5, 25, 10]
print(bigger_smaller(a_list))
