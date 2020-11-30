import csv

with open('font3.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('font3.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('value', 'Key'))
        writer.writerows(lines)