import csv
import json

"""
This python file aims to get the json file from these csv files
"""


def jsonprocess():

    """
    把每个社区的总大小显示出来真的有必要吗？
    jsonFile = {"neighbour1": {
                    "totalNumber":555.
                    "top5":{
                    "caegory":22,
                    "category":33,
                    ...
                    }
                },
                ...
                }

    :return:
    """

    jsonFile = {}
    with open("./ccsFiles/top5_NewYorkCity_1.csv", "r") as f:
        seatleCsv = csv.reader(f)               #记一下csv的读写方法，到这儿还是忘记了
        try:
            next(seatleCsv)                         #next不是csv的专有用法，不能用 csv.next()；看清楚是读文件还是写文件
        except Exception as e:                         #这里一开始没有写as为什么要写as呢？
            print(e)

        for line in seatleCsv:
            #判断该社区是否已经存在
            if line[0] in jsonFile:                 #python3判断字典里是否有某一个键值
                jsonFile[line[0]]["top5"][line[2]] = int(line[3])
            else:
                #不存在，就新建一个
                jsonFile[line[0]] = {"totalNumber": int(line[4]), "top5": {line[2]: int(line[3])}}

        print(jsonFile)

    #对字典进行排序   这里要记一下，根据键或者值
    print(jsonFile.items())
    jsonFile = dict(sorted(jsonFile.items(), key=lambda it:int(it[1]["totalNumber"])))

    #将python对象写入文件
    with open("./ccsFiles/NewYorkCity.json", "w") as f:
        json.dump(jsonFile, f, indent=2)                #indent = 2加上后，神奇的事情就发生了！ 太奇妙了


if __name__ == "__main__":
    jsonprocess()
