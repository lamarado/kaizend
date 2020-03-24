import csv
import json

with open('sample_products.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

#with open('/temp/file.csv', 'w', newline='') as f:
#    writer = csv.writer(f)
#    writer.writerows(iterable)

with open('/Users/lamarado/Downloads/Keys/gpayroll-964-490e9a520891.json', 'r') as f:
    data = json.load(f)
    print(data)
