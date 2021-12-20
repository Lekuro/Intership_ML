def f1(x):
    # try:
    return x/(x+100)
    # except ZeroDivisionError as e:
    #     print('exception: ', e)


def f2(x):
    # try:
    return 1/x
    # except ZeroDivisionError as e:
    #     print('exception: ', e)


def f3(x):
    try:
        return 20*(f1(x)+f2(x))/x
    except ZeroDivisionError as e:
        print('exception: ', e)


print(f3(0))
