# This is a sample Python script.

import csv

def main():
    neighbors = []               #社区的数量
    neighborsNum = []            #每个社区出现的次数
    stores = []                  #所有出现的商店种类
    storesNum = []               #统计不同类型的商店出现的次数；与上面一一对应
    storesTotalNum = []          #统计每个不同类型的商店总个数
    storesNumperNeighbor = []    #统计每个社区里商店的个数

    #去重

    try:
        with open('./ccsFiles/top5_NewYorkCity.csv') as seattleF:      #with可以自己关闭文件
            #写入新文件
            seattleF_csv = csv.reader(seattleF)
            newRows = []

            for line in seattleF_csv:
                if line not in newRows:
                    newRows.append(line)

            with open('./ccsFiles/top5_NewYorkCity_1.csv', 'w') as seattleF_1:     #只使用w会有空行
                seaWriter = csv.writer(seattleF_1, lineterminator='\n')
                seaWriter.writerows(newRows)

            seattleF_csv = csv.reader(seattleF)
            next(seattleF_csv)                                     #next() 返回迭代器的下一个项目。next() 函数要和生成迭代器的iter() 函数一起使用。
            for line in seattleF_csv:
                if line[0] not in neighbors:
                    neighbors.append(line[0])
                    storesNumperNeighbor.append(int(line[4]))
                    neighborsNum.append(1)
                else:
                    neighborsNum[neighbors.index(line[0])] += 1
                    if neighborsNum[neighbors.index(line[0])] > 5:
                        print("重复项", line)

                if line[2] not in stores:
                    stores.append(line[2])
                    storesNum.append(1)
                    storesTotalNum.append(int(line[5]))
                else:
                    storesNum[stores.index(line[2])] += 1

    except Exception as e:
        print(e)                                                    #即使没有写出异常的名称也会抛出异常  其次不知道异常的名字这儿也可以自己显示出来

    """
    多行注释用三个单引号或者三个双引号将注释括起来，例如:
    python3中默认是换行；要想不换行你应该写成 print(i, end = '' ) 
    print可以输出字符串，变量，list 字典等等，也可以格式化输出
    print("变量1", file_name, "变量2", new_name)
    print("变量1：%s 变量2：%s" % (file_name, new_name))
    """
    print("社区数量：", len(neighbors))
    print("社区：", neighbors)
    print("各社区的数量", neighborsNum)
    print("出现的商店类型：", stores)
    print("出现的商店类型的数量：", len(stores))
    storesNum.sort()                #排序函数
    print("对应的商店数量：", storesNum)
    storesNumperNeighbor.sort()
    print("每个社区对应的商店数量：", storesNumperNeighbor)
    storesTotalNum.sort()
    print("每种商店类型对应的个数：", storesTotalNum)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

