import csv
rows = []
with open("midas-open_uk-daily-temperature-obs_dv-202207_caithness_00032_wick-airport_qcv-1_2021.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
#print(header)
print(rows)