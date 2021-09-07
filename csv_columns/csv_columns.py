import csv
from itertools import zip_longest
# DictReader

def csv_columns(csv_file, *, headers=None, missing=None):
    csv_data = csv.reader(csv_file)
    # headers = next(reader) można użyć wcelu zdopycia pierwszej wartości
    if not headers:
        headers, *csv_data = csv_data
    # when * is used, it will break the csv_data list, and act like we pased to zip argument multiple list,
    # so it will pair 0 with 0 argument in second list etc... tuple unpacking
    return {key: val for key, *val in zip_longest(headers, *csv_data, fillvalue=missing)}


# Trays Solutions
#
# def csv_columns(rows, *, headers=None, missing=None):
#     """Return dictionary mapping headers to corresponding columns."""
#     reader = csv.reader(rows)
#     if headers is None:
#         headers = next(reader)
#     columns = zip_longest(*reader, fillvalue=missing)
#     return {
#         header: list(column)
#         for header, column in zip(headers, columns)
#     }
#
#
#      wykorzystanie dic reader oraz defoult dick, warto w przyszłości się temu przyjrzeć
# from collections import defaultdict
# from csv import DictReader
#
#
# def csv_columns(rows, *, headers=None, missing=None):
#     columns = defaultdict(list)
#     reader = DictReader(rows, fieldnames=headers, restval=missing)
#     for row in reader:
#         for name, value in row.items():
#             columns[name].append(value)
#     return columns
