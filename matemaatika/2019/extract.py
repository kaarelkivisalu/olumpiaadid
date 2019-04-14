import json
import csv

data = []

for age_grp in range(9, 13):
    i = 1
    prev_points = 0
    prev_placement = 1
    with open(f"{age_grp}kl.txt") as f:
        for row in csv.reader(f, dialect="excel-tab"):
            print(row)
            name = row[0]
            cls = int(row[2])
            score = int(row[5])
            school = row[1]
            if score == prev_points:
                placement = prev_placement
            else:
                placement = prev_placement = i
                prev_points = score
            data.append({"name":name,"class":cls,"age_group":str(age_grp),"score":score,"school":school,"placement":placement})

with open("../2019.json",'w') as f:
    d = {
        "age_groups": [{"name":str(x),"min_class":x,"max_class":x}for x in range(9,13)],
        "scores": data
    }
    json.dump(d, f)
