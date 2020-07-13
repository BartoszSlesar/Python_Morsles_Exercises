import csv
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('--in-delimiter',dest='delim')
parser.add_argument('old_file')
parser.add_argument('new_file')
parser.add_argument('--in-quote',dest='quote')

args = parser.parse_args()

with open(args.old_file,'rt') as old_file:
    arguments = {}
    if args.delim:
        arguments['delimiter'] = args.delim
    if args.quote:
        arguments['quotechar'] = args.quote
    if not args.delim:
       arguments['dialect'] = csv.Sniffer().sniff(old_file.read())
       old_file.seek(0)
    reader = csv.reader(old_file,**arguments)
    list_contect = [word for word in reader]
with open(args.new_file,'wt',newline='') as new_file:
    csv.writer(new_file,delimiter=',').writerows(list_contect)
