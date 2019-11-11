def sort(a_list):
    new_list = []
    number_now = 0
    for i in range(len(a_list)):
        number_now = min(a_list)
        a_list.remove(number_now)
        new_list.append(number_now)
    return new_list
a_list = [40, 100, 1, 5, 25, 10]
print(sort(a_list))