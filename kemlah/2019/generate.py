import json, csv, re, os

data = {
    "age_groups": [{
        "name": "noorem",
        "min_class": 9,
        "max_class": 10,
        "ex_labels": [f"Ül {x}" for x in range(1, 10)]
    }, {
        "name": "vanem",
        "min_class": 11,
        "max_class": 12,
        "ex_labels": [f"Ül {x}" for x in range(1, 10)]
    }],
    "scores": []
}

def main():
    for fname in sorted(os.listdir(".")):
        if not fname.endswith(".csv"):
            continue
        match = re.match(r"klv26(.)rt_p(.).csv", fname)
        age_group = "noorem" if match[1] == "n" else "vanem"
        page = match[2]
        with open(fname) as f:
            for row in csv.reader(f):
                placement = int(re.match(r"(\d+).*", row[0])[1])
                name = row[1]
                try:
                    cls = int(row[2])
                except:
                    cls = None
                school = row[3]
                teacher = row[4].split(', ') if row[4] != '-' else []
                scores_per_ex = map(float, row[5:-1])
                total_score = float(row[-1])
                d = {
                    "name": name,
                    "class": cls,
                    "age_group": age_group,
                    "score": total_score,
                    "placement": placement,
                    "school": school,
                    "instructors": teacher,
                    "scores_per_ex": list(scores_per_ex),
                    "rank": None,
                }
                data['scores'].append(d)
    with open("../2019.json", 'w') as f:
        json.dump(data, f)

if __name__ == "__main__":
    main()
