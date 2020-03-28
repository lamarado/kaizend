# Kaizend 3: Python for Scripting - Exercises

# Exercise: Products CSV Reader and Writer

# The main objective of this project idea is to read a CSV with a list of
# products for an ecommerce site. The application should be able to:

# - Remove all products that don’t have categories
# - Output a new CSV file that contains all products that have categories
# - Use argparse for passing the filename of the CSV input file
# - Prompt the user to specify the filename of the CSV output file
# - Name the exercise file products_csv_parser.py
# - Fix flake8 errors (if you don’t know how to do this yet, refer to
#   How to Use Flake8 Guide)

import argparse
import csv
import sys

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='CSV file to read')
args = parser.parse_args()

output_filename = input("Please specify filename of the output CSV file: ")
output_file_ext = output_filename[-4:].lower()
default_file_ext = ".csv"

if output_file_ext != default_file_ext:
    output_filename += default_file_ext

try:
    file = open(args.filename)
except FileNotFoundError as err:
    print(f"Error: {err}")
    ERROR_RETURN = 1
    sys.exit(ERROR_RETURN)
else:
    valid_products = []
    with open(args.filename, newline='') as f:
        reader = csv.reader(f)
        rows = list(map(tuple, reader))
        CATEGORIES_COLUMN = 25
        valid_products = [row for row in rows if row[CATEGORIES_COLUMN] != '']
    with open(output_filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(valid_products)
        print(f"Output saved on {output_filename}.")
