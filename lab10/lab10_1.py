import csv

with open('2000_boysNames.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('2000_boysNames.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('First Name', 'Count'))
        writer.writerows(lines)

# import csv

with open('2000_GirlsNames.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('2000_GirlsNames.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('First Name', 'Count'))
        writer.writerows(lines)
