#!/usr/bin/end python3
from bs4 import BeautifulSoup as bs
import os
import json
import collections
import re

def extract_table(tbl_elem):
    out_rows = []
    for row in tbl_elem.find_all("tr"):
        out_cols = []
        for col in row.find_all("td"):
            out_cols.append(col.get_text().strip())
        out_rows.append(out_cols)
    return out_rows

data = collections.defaultdict(lambda: [])
point_list = []

other_class_markers = {
    "2007_9.html": "8",
    "2007_12.html": "12",
    "2008_10.html": "9",
}

cls_regex = r"\((\d+)\. ?kl(ass|\.)?\)"

for x in os.listdir("pdf"):
    if not x.endswith(".html"):
        continue
    with open("pdf/"+x, encoding="windows-1257") as f:
        year = int(x.split("_")[0])
        def_cls = int(x.split("_")[1].split(".html")[0])
        soup = bs(f.read(), "lxml")
        skipped_rows = 0
        i = 1
        prev_points = 0
        prev_placement = 1
        tbl = extract_table(soup.table)
        for row in tbl:
            if row[0] == "Nimi" or row[0] == "" or row[0] == "Õpilase nimi":
                skipped_rows += 1
                continue
            name = row[0]
            school = row[1]
            if len(row) == 9:
                total_index = 7
            elif len(row) == 8:
                total_index = 7
            elif len(row) == 10:
                total_index = 8
            else:
                continue
            ex_start_index = total_index - 5
            try:
                if row[total_index] == "18+x":
                    points = 18
                else:
                    points = int(row[total_index])
            except:
                print(x, i, row[total_index])
                raise
            ex_pts = []
            for ex_col in range(ex_start_index, ex_start_index+5):
                pts_str = row[ex_col]
                if pts_str in ("", "-", "‒", "–","—", "x"):
                    pts = 0
                else:
                    try:
                        pts = int(pts_str)
                    except:
                        print(x, i, row[col_index])
                        raise
                ex_pts.append(pts)

            if points == prev_points:
                placement = prev_placement
            else:
                placement = i
                prev_placement = i
                prev_points = points
            cls = def_cls
            cls_special = re.search(cls_regex, name)
            if cls_special:
                cls = int(cls_special[1])
                name = re.sub(cls_regex, "", name).strip()
            if name[-2:] == "**":
                name = name[:-2]
            elif name[-1] == '*' and x in other_class_markers:
                name = name[:-1]
                cls = other_class_markers[x]
            elif name[-1] == '*':
                name = name[:-1]
            data[year].append({
                "name":name,
                "class":cls,
                "age_group":str(def_cls),
                "score":points,
                "school":school,
                "placement":placement,
                "scores_per_ex": ex_pts,
            })
            i += 1
    if skipped_rows > 3:
        print(f"Warning: more than 3 rows skipped in {x}")

for k,v in data.items():
    with open(f"{k}.json", 'w') as f:
        d = {
            "age_groups": [{
                "name":str(x),
                "min_class":x,
                "max_class":x,
                # matemaatika olümpiaadil on *alati* olnud 5 ülesannet
                "ex_labels": ["1.","2.","3.","4.","5."]
            } for x in range(9, 13)],
            "scores": v
        }
        json.dump(d, f)
