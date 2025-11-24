import os
import csv

here = os.path.dirname(__file__)
path = os.path.join(here, "athletes.csv")

Long_Jump = [ ]
Triple_Jump = [ ]
High_Jump = [ ]
Pole_Vault = [ ]
Run1 = [ ]
Run2 = [ ]
Run4 = [ ]
Run8 = [ ]
Run16 = [ ]

first_col = []
with open(path, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    # next(reader, None)  # hoppa header om behövs
    for row in reader:
        if row:
            first_col.append(row[4])
print(first_col)