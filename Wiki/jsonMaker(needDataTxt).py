import re, json, os

# 현재 월
month = "3"

try :
    os.mkdir(month+"월")
except :
    pass

t = len(os.listdir(month+"월"))+1
fileName = f"{month}월/{t}d.json"

with open("data.txt", "r") as f :
    dumpstr = f.read().strip()

splitData = re.compile(r".*\d+년 - ")
DataArray = dumpstr.split("\n")
makeDictionary = {"기념일":[], "사건":{}}
tmpKey = None
isMultiline = False # 멀티라인 불리언
for i in range(len(DataArray)) :
    line = DataArray[i].strip()
    if re.match("^.*\d+년 - ", line) != None :
        # tmp = re.search("(.*) - (.*)", line)
        # makeDictionary["사건"][tmp.group(1)] = tmp.group(2)
        tmp = re.split(r" - ", line, maxsplit=1)
        makeDictionary["사건"][tmp[0]] = tmp[1]
        isMultiline = False
    else :
        if isMultiline :
            makeDictionary["사건"][tmpKey].append(line)
            try :
                if re.match("^.*\d+년$", DataArray[i+1].strip()) != None :
                    isMultiline = False
            except :
                pass
        else :
            if re.match("^.*\d+년$", line) != None :
                isMultiline = True
                tmpKey = line
                makeDictionary["사건"][tmpKey] = []
            else :
                isMultiline = False

print("key 갯수 :",len(makeDictionary["사건"].keys()))
data = json.dumps(makeDictionary, ensure_ascii=False)
# print(data)
with open(fileName, "w") as t :
    t.write(data)