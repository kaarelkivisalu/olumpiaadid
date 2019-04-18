#!/usr/bin/env python3

import collections
from decimal import Decimal
import simplejson as json
import csv
import os
import re

def parse_first_col(val):
    val = val.replace("\N{EN DASH}", "-").replace(".", '')
    if "-" in val:
        if val.count("-") > 1:
            return None
        a,b = val.split("-")
        if not (a.isdigit() and b.isdigit()):
            return None
        return int(a)
    else:
        if not val.isdigit():
            return None # also reaches here if val is an empty string
        return int(val)

def is_proper_name(val):
    lowercase_special_cases = ["al", "nim", "i", "nimeline"]
    d = False
    for x in re.split(r"\W", val):
        d = True
        if (x.capitalize() != x) and not (x.isupper() and len(x) < 4) and x not in lowercase_special_cases:
            return False
    return d

star_classes = {
    "eko51v3k10tul.csv": None,
    "eko55v3k12tul.csv": None,
    "eko52v3k10tul.csv": 9,
}
class_exception_regex = r"\((\d+)\.? ?kl(ass|\.)?\)"

years = collections.defaultdict(lambda: [])

line_parse_modes = [
    ["1","2","3","4","5","6","Teooria","Praktika"],
    ["1","2","3","4","5","6","Tüvenumbrid","Teooria","Praktika"],
    [str(x) for x in range(1, 10)]+["6 parimat", "Praktika"],
    ["1","2","3","4","5","6","Teooria", "Teooria (max 60)", "Praktika"],
]

age_group_parse_modes = dict()

def main():
    for fname in sorted(os.listdir("pdf")):
        if not fname.endswith(".csv"):
            continue
        match = re.match(r"eko(\d+)v3k(\d+)tul\.csv", fname)
        if not match:
            raise Exception(f"invalid filename {x}")
        age_group = int(match[2])
        # year before first olympiad
        year = int(match[1])+1953
        seen_parse_modes = set()
        num_ok_rows = 0
        with open("pdf/"+fname) as f:
            for row in csv.reader(f):
                if len(row) == 0:
                    continue
                placement = parse_first_col(row[0])
                if placement is None:
                    if num_ok_rows > 0:
                        print(f"Warning: skipped line not at beginning of file in {fname}")
                    continue
                cls = age_group
                name = row[1].replace("\n"," ")
                if name.endswith("*"):
                    if fname in star_classes:
                        if star_classes[fname] is not None:
                            cls = star_classes[fname]
                        name = name[:-1]
                    else:
                        print(f"Special attention needed: {name} from {fname}")
                match = re.search(class_exception_regex, name)
                if match:
                    cls = int(match[1])
                    name = re.sub(class_exception_regex, "", name).strip()
                # if re.search(r"[^a-zA-ZõäöüÕÄÖÜšžŠŽ -]", name):
                #     print(f"Weird name: {name} from {fname}")
                school = row[2]
                teacher_name = row[3]
                # if not is_proper_name(name):
                #     print(f"Warning: {name} (from {fname}) doesn't look like a proper name")
                # if not is_proper_name(school):
                #     print(f"Warning: {school} (from {fname}) doesn't look like a proper name")
                if teacher_name == "":
                    print(f"Warning: no teacher name in row {placement} of {fname}")
                if school == "": print(f"Warning: empty school name in {fname} line {placement}")
                if name == "": print(f"Warning: empty name in {fname} line {placement}")
                if len(row) not in (13, 14, 15, 17):
                    print(f"Error: weird size row ({len(row)}) in {fname}")
                    continue
                # in 2015, there was a separate column for "significant figures" and no column for "award"
                # 2014 just had a normal column for significant figures
                if len(row) in (14, 17) and year != 2015:
                    if row[-1] not in ("I", "II", "III", "Järk", "", "I järk", "II järk", "III järk"):
                        print(f"Warning: weird final row in {fname} line {placement}")
                if year in (2014, 2015):
                    line_parse_mode = 1
                elif len(row) in (13, 14):
                    line_parse_mode = 0
                elif len(row) == 17:
                    line_parse_mode = 2
                elif len(row) == 15:
                    # has a silly thing where theory points are rescaled from max 65 points to max 60 points, then prax points added
                    line_parse_mode = 3
                if len(seen_parse_modes) > 0 and line_parse_mode not in seen_parse_modes:
                    print(f"Warning: conflicting parse modes ({seen_parse_modes} vs {line_parse_mode}) in {fname}")
                seen_parse_modes.add(line_parse_mode)
                num_exs = len(line_parse_modes[line_parse_mode])
                total_points_col = num_exs + 4
                exs_points = []
                not_ok = False
                for x in range(num_exs):
                    val = row[x+4]
                    if val in ("", "-"):
                        exs_points.append(0)
                        continue
                    if " " in val:
                        print(f"Error: space in points in {fname} line {placement}")
                        not_ok = True
                        break
                    try:
                        pts = Decimal(val.replace(",","."))
                        if pts > 100:
                            print(f"Warning: quite a lot of points in {fname} line {placement}")
                        exs_points.append(pts)
                    except:
                        not_ok = True
                        break
                if not_ok:
                    continue
                if row[total_points_col] == "":
                    total_points = exs_points[-2] # use theory points instead
                else:
                    try:
                        total_points = Decimal(row[total_points_col].replace(",","."))
                    except:
                        print(f"Error extracting total points from {fname} line {placement}")
                        continue
                d = {
                    "name": name,
                    "class": cls,
                    "age_group": str(age_group),
                    "score": total_points,
                    "placement": placement,
                    "school": school,
                    "scores_per_ex": exs_points,
                }
                years[year].append(d)
                num_ok_rows += 1
        if num_ok_rows == 0:
            print(f"Error: no valid rows in {fname}")
            continue
        elif num_ok_rows < 17:
            print(f"Warning: few rows in {fname} ({num_ok_rows}, expected >=17)")
        # should every only get 1 member so pop should be safe
        try:
            age_group_parse_modes[(year, age_group)] = seen_parse_modes.pop()
        except:
            print(f"error in {fname}")
            raise


    for k,v in years.items():
        with open(f"{k}.json",'w') as f:
            age_groups = []
            for x in age_group_parse_modes:
                if x[0] == k:
                    age_groups.append({
                        "name": str(x[1]),
                        "min_class":x[1],
                        "max_class":x[1],
                        "ex_labels": line_parse_modes[age_group_parse_modes[x]]
                    })
            d = {
                "age_groups": age_groups,
                "scores": v
            }
            json.dump(d, f)

if __name__ == "__main__":
    main()

