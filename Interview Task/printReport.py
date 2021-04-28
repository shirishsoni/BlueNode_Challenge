import csv
from decouple import config
def report(report):
    with open(config('REPORT'), "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(report)