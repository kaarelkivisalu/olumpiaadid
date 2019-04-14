#!/usr/bin/end python3
from bs4 import BeautifulSoup as bs
import os
import json
import collections
import re

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
        i = 1
        prev_points = 0
        prev_placement = 1
        for row in soup.table:
            if isinstance(row, str):
                continue
            first_txt = row.td.get_text().strip()
            if first_txt == "Nimi" or first_txt == "" or first_txt == "Õpilase nimi":
                continue
            tds = row.find_all("td")
            name = tds[0].get_text().strip()
            school = tds[1].get_text().strip()
            if len(tds) == 9:
                col_index = 7
            elif len(tds) == 8:
                col_index = 7
            elif len(tds) == 10:
                col_index = 8
            else:
                continue
            try:
                if tds[col_index].get_text().strip() == "18+x":
                    points = 18
                else:
                    points = int(tds[col_index].get_text().strip())
            except:
                print(x, i, tds[col_index].get_text())
                raise
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
            data[year].append({"name":name,"class":cls,"age_group":str(def_cls),"score":points,"school":school,"placement":placement})
            i += 1

for k,v in data.items():
    with open(f"{k}.json", 'w') as f:
        d = {
            "age_groups": [{"name":str(x),"min_class":x,"max_class":x} for x in range(9, 13)],
            "scores": v
        }
        json.dump(d, f)
