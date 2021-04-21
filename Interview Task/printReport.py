import csv

def report(report):
    with open("out.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(report)