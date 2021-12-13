data = [[1, 3, 3, 4], [2, 1, 3, 5], [4, 0, 1, 7], [5, 2, 1, 0], [0, 4, 8, 3]]


def raise_index_out_of_range(data, index):
    len_inside = len(data[0])
    if index not in range(len_inside):
        raise ValueError(
            f'Your index {index} is out of possible range from 0 to {len_inside-1}')


def sort_by_index(data, sorted_index=1):
    raise_index_out_of_range(data, sorted_index)
    return sorted(data, key=lambda d: d[sorted_index])


def create_dict(data, key_index=1):
    raise_index_out_of_range(data, key_index)
    return {item[key_index]: item[:key_index]+item[key_index+1:] for item in data}


def sort_dict_value(data, reversed=True):
    return {key: sorted(value, reverse=reversed) for key, value in data.items()}


def get_set_from_dict_values(data):
    return {item for values in data.values() for item in values}


def get_str_from_set(data):
    list_of_str = [str(item) for item in data]
    set_of_str = {str(item) for item in data}
    return f"from list: {''.join(list_of_str)}, from set: {''.join(set_of_str)}"


print('data: ', data)
result1 = sort_by_index(data)
print('task1: ', result1)
result2 = create_dict(result1)
print('task2: ', result2)
result3 = sort_dict_value(result2)
print('task3: ', result3)
result4 = get_set_from_dict_values(result3)
print('task4: ', result4)
result5 = get_str_from_set(result4)
print('task5: ', result5)
