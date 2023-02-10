import os, re

month = "12"

fileList = os.listdir(month+"m")
os.chdir(month+"m")
for i in range(len(fileList)) :
    date = re.search(r"\d+월 (\d+)일.txt", fileList[i]).group(1)
    os.rename(fileList[i], f"{month.zfill(2)}{date.zfill(2)}.txt")