import csv
from argparse import ArgumentParser


def slice(line, end_start):
    return [line[start:end].strip() for start, end in end_start]


def parse_fixed_width_file(file, slice_rows):
    for row in file.readlines():
        yield slice(row, slice_rows)


def parse_columns(slice_rows):
    splited = [val.split(":") for val in slice_rows.split(",")]
    return [(int(a), int(b)) for a, b in splited]


def arg_parser(presented_values):
    parser = ArgumentParser()
    parser.add_argument('text_file')
    parser.add_argument('csv_file')
    parser.add_argument('--cols', dest='columns', required=True)
    return parser.parse_args(presented_values)


def main(presented_values):
    args = arg_parser(presented_values)
    slice_rows = parse_columns(args.columns)
    with open(args.text_file, 'rt') as text_file:
        parsed_file = parse_fixed_width_file(text_file, slice_rows)
        with open(args.csv_file, 'wt', newline='') as csv_file:
            csv.writer(csv_file, delimiter=',').writerows(parsed_file)


