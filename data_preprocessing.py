import csv

# Open input CSV file as source
# Open output CSV file as result
with open("raw_diabetes.csv", "r") as source:
    reader = csv.reader(source)

    with open("diabetes.csv", "w") as result:
        next(source)
        writer = csv.writer(result)
        for r in reader:
            writer.writerow((r[5], r[6], r[7], r[8]))