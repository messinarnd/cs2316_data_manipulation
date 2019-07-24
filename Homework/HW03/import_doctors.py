import sys
import csv

patients = {}
with open(sys.argv[1], newline='') as fin:
    next(fin)
    csvin = csv.reader(fin)
    for row in csvin:
        patients[row[0]] = row[1]

    print(patients)
