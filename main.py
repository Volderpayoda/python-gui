import CSV
with open('iris.csv', ‘rb’) as f:
reader = csv.reader(f)
for row in reader:
print row