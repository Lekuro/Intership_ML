import csv
import json
generator_5_90 = (x for x in range(5, 91))


def generator_from_to(from_=5, to=90):
    for i in range(from_, to+1):
        yield i


def f1(x): return x/(x+100)
def f2(x): return 1/x


def f3(x):
    try:
        return 20*(f1(x)+f2(x))/x
    except ZeroDivisionError as e:
        print('exception: ', e)


def result_to_dict(set_range, *funcs):
    return {x: {f(x) for f in funcs} for x in set_range}


def dict_to_csv(data_dict):
    with open('lesson_03_file_func_mod/results.csv', 'w') as file_csv:
        csv_writer = csv.writer(file_csv, delimiter=';',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["x", "f1(x)", "f2(x)", "f3(x)"])
        for key, values in data_dict.items():
            csv_writer.writerow([key, *values])


def list_from_csv(file_name):
    result = []
    with open(file_name) as file_csv:
        csv_reader = csv.reader(file_csv, delimiter=';',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in csv_reader:
            if row:
                result.append(row)
    return result


def list_to_json(data_list):
    with open('lesson_03_file_func_mod/results.json', 'w') as file_json:
        json.dump(data_list, file_json, indent=4)


print(result_to_dict(generator_5_90, f1, f2, f3))
dict_to_csv(result_to_dict(generator_from_to(), f1, f2, f3))
print(list_from_csv('lesson_03_file_func_mod/results.csv'))
list_to_json(list_from_csv('lesson_03_file_func_mod/results.csv'))


# def list_to_json_my(data_list):
#     len_data = len(data_list)
#     result = {i-1: dict(zip(data_list[0], data_list[i]))
#               for i in range(1, len_data)}
#     # for i in range(1, len_data):
#     #     result.update({i-1: dict(zip(data_list[0], data_list[i]))})
#     with open('lesson_03_file_func_mod/results_my.json', 'w') as file_json:
#         json.dump(result, file_json, indent=4)
# list_to_json_my(list_from_csv('lesson_03_file_func_mod/results.csv'))
