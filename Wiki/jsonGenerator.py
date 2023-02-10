import re, json, os

# 현재 월
month = "5"

# 폴더생성
try :
    os.mkdir(month+"월")
except :
    pass



def makeDict(fileName) :
    try :
        with open(f"{month}me/{fileName}", "r") as fi :
            dumpstr = fi.read()
        document = dumpstr.split("기념일 및 절기")
        EVENT = document[0].strip()
        ANNIVERSARY = document[1].strip()
        
        DataArray = EVENT.split("\n")
        makeDictionary = {"기념일":[], "사건":{}}
        tmpKey = None
        isMultiline = False # 멀티라인 불리언

        for i in list(filter(None, ANNIVERSARY.split("\n"))) :
            makeDictionary["기념일"].append(i)
        for i in range(len(DataArray)) :
            line = DataArray[i].strip()
            if re.match("^.*\d+년 - ", line) != None :
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
        print(f"{fileName} ", end="")
        print("\tkey 갯수 :",len(makeDictionary["사건"].keys()), end="")
        print("\tarray 갯수 :",len(makeDictionary["기념일"]))
        data = json.dumps(makeDictionary, ensure_ascii=False)
        # print(data)
        tmp = fileName.split(".txt")[0]
        with open(f"{month}월/{tmp}.json", "w") as t :
            t.write(data)
    except :
        print("ERROR :",fileName)



for i in os.listdir(month+"me") :
    makeDict(i)
print("생성된 파일 개수 :",len(os.listdir(month+"월")))