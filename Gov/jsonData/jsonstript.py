import json

f = open("행정부.json", "r")
anni_json = json.load(f)
f.close()

res = {}
for i in anni_json.keys() :
    tmp = {}
    for l in anni_json[i].keys() :
        tmp[l.strip()] = anni_json[i][l].strip()
    res[i.strip()] = tmp
w = open("h.json", "w")
t = json.dumps(res, ensure_ascii=False)
w.write(t)
w.close()
