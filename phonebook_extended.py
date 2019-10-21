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

for row in reader:
    name = row["name"]
    number = row["number"]
    if name == name_in:
        print(f"{name}'s phone number is {number}")
        f.close()
        sys.exit(0)
print(f"{name_in} is not in the phonebook.")

f.close()