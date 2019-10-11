import re,json

data = {
    "age_groups": [{
        "name": "noorem",
        "min_class": 9,
        "max_class": 10,
        "ex_labels": [f"Ül {x}" for x in range(1, 7)]
    }, {
        "name": "vanem",
        "min_class": 11,
        "max_class": 12,
        "ex_labels": [f"Ül {x}" for x in range(1, 7)]
    }],
    "scores": []
}

for v in "nv":
    with open("lvs19_"+v+".txt") as f:
        lines = [re.split(r'\s\s+', x.strip()) for x in f.read().strip().split('\n')]
    for x in lines:
        placement, _, name = x[0].partition(" ")
        school = x[1]
        cls = x[2]
        teacher = x[3]
        scores_per_ex = list(map(lambda x: int(x.replace('–','0')), x[4:4+6]))
        print(x)
        total = x[10]
        rank = x[11] if len(x) == 12 else ""
        data["scores"].append({
            "name": name,
            "class": int(cls),
            "age_group": "noorem" if v == "n" else "vanem",
            "score": int(total),
            "placement": int(placement),
            "rank": rank,
            "school": school,
            "instructors": [teacher],
            "scores_per_ex": scores_per_ex
        })
with open("2019.json", 'w') as f:
    json.dump(data, f)
