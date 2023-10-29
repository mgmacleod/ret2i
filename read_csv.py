import csv
from collections import defaultdict


def read_csv(filepath):
    data = []
    with open(filepath, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append((row["prompt"], row["filename"]))
    return dict(zip(*data))


print(read_csv("/home/mgm/development/code/ret2i/log_wavy.csv"))
