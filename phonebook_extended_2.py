import csv
import sys
from cs50 import get_string

if len(sys.argv) != 2:
    sys.exit("Usage: python phonebook.py data.csv")

f = open(sys.argv[1])
reader = csv.DictReader(f)

fields = reader.fieldnames
if "name" not in fields or "number" not in fields:
    sys.exit("File must have name and number columns")

name_in = get_string("Name: ")

people = {row["name"]: row["number"] for row in reader}

if name_in in people:
    print(f"{name_in}'s number is {people[name_in]}")
else:
    print(f"{name_in} is not in the phonebook.")

f.close()