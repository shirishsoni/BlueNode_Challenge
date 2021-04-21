import csv

def report(report):
    with open("Report.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(report)