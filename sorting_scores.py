import csv

passing = []
failing = []
scores = []
average = 0

filepath = "student_test_scores.csv"
with open(filepath, "r", newline="") as file:
    content = csv.DictReader(file)
    for line in content:
        if int(line["Test Score"]) == 100:
            print(line)
        if int(line["Test Score"]) == 0:
            print(line)
        if int(line["Test Score"]) >= 70:
            passing.append(line)
            scores.append(int(line["Test Score"]))
        else:
            failing.append(line)
            scores.append(int(line["Test Score"]))

with open("Passing.csv", "w", newline= "") as file:
    writer = csv.writer(file)
    writer.writerow(passing)

with open("Failing.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(failing)

for line in scores:
    average+=line
average= average/len(scores)
print(average)