import sys, os

def fileExtract(month, fileName) :
    try :
        with open(f"{month}m/{fileName}", "r") as fi :
            dumpstr = fi.readlines()
        with open(f"{month}me/{fileName}", "w") as f :
            isEvent = False
            isAnni = False
            for i in range(len(dumpstr)) :
                line = dumpstr[i].rstrip()
                if line == "사건" :
                    isEvent = True
                elif line == "기념일 및 절기" :
                    isEvent = False
                    isAnni = True
                elif line == "축일" :
                    isAnni = False
                if isEvent : # 사건 키워드 이후 라인을 입력
                    if line != "실제" and line != "사건":
                        if line == "가상" :
                            isEvent = False
                        else :
                            f.write(line+"\n")
                if isAnni :
                    if line == "축일" :
                        isAnni = False
                    else :
                        f.write(line+"\n")
    except :
        print(fileName)
    

month = 4

try :
    os.mkdir(f"{month}me")
except :
    pass

for file in os.listdir(f"{month}m") :
    # fileExtract(month, file)
    print(file)