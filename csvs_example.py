import csv
import sys

if len(sys.argv) != 2:
    sys.exit("Usage: python example.py data.csv")

f = open(sys.argv[1])
reader = csv.DictReader(f)
categories = reader.fieldnames
#print(categories)
# Create new list
points = []
# Create new Dictionary
team_points = {}

# Iterate over rows of csv
for row in reader:
    # Add number of points to list
    points.append(int(row["Points"]))
    # Create new dictionary where key is team name, value is points
    team_points[row["Team"]] = int(row["Points"])
print(team_points["Liverpool"])

f.close()
