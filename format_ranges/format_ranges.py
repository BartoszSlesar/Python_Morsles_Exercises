from collections import Counter


def format_ranges(numbers):
    # first, *rest = numbers
    continuous = continuous_numbers(numbers)
    # for val in continuous:
    result = ','.join(f'{val[0]}-{val[-1]}' if len(val) > 1 else f'{val[0]}' for val in continuous)
    # end = 0
    # check = first
    # result = ''
    # for val in rest:
    #     if (val - check) == 1:
    #         end = val
    #         check = val
    #     elif end != 0:
    #         result = result + f'{first}-{end},'
    #         first = val
    #         check = val
    #         end = 0
    #     else:
    #         result = result + f'{first},'
    #         check = val
    #         first = val
    #
    # if end != 0:
    #     result = result + f'{first}-{end}'
    # else:
    #     result = result + f'{first}'
    return result


def continuous_numbers(lis):
    '''this function will return list of list continuous numbers from given list'''
    if not lis:
        return lis

    # sortuje liste jak funkcja natomiast lista.sort() sortuje oryginał,niektóre iteratory nie posiadają tej funkcji
    # przez co mogą zwracać błąd
    lis = sorted(lis)
    first, *rest = lis
    test = [first]
    result = []
    duplicates = []
    for val in rest:
        # filtruje duplikaty, do oddzielnej listy, którą następnie przeprocesowuje tak samo czyli rekurencja
        if (val - test[-1]) == 0:
            duplicates.append(val)
        elif (val - test[-1]) != 1:
            result.append(test)
            test = [val]
        else:
            test.append(val)
    result.append(test)
    if duplicates:
        result = result + continuous_numbers(duplicates)
        result = sorted(result)
    print(result)
    return result


print(format_ranges([1, 9, 1, 7, 3, 8, 2, 4, 2, 4, 7]))
