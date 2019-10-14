# hamming code

def islegal(string):
    return string.count('1')+string.count('0') == len(string)


def toBin(n):  # 十进制转二进制
    result = '0'
    if n == 0:
        return result
    else:
        result = toBin(n // 2)
        return result + str(n % 2)


def smallest_check_number(k):
    r = 1
    while 2 ** r - r - 1 < k:
        r += 1
    return r


def toHamming(hammingList):
    hList = []
    for i in str(hammingList):
        hList.append(int(i))         # 转换为列表

    # print(smallest_check_number(len(hList)))
    for j in range(smallest_check_number(len(hList))):   # 插入海明检验码的位置
        hList.insert(2**j-1,"a"+str(2**j-1))
    print("hList:",hList)

    checkIndex = 0
    bListLen = 0
    List = []
    for a in range(len(hList)):
        b=toBin(a+1).zfill(int(len(hList)/2))   #不足补零
        # print("b",b)
        blist=[]
        for i in str(b):
            blist.append(int(i))
        List.append(blist)
        checkIndex = len(blist)-1
        bListLen = len(blist)
        # print("blist"+str(a),blist)

    # print("\ncheckINdex:",checkIndex,bListLen,"\n")

    # checkindex 已经改为blist的长度-1
    while checkIndex>0:
        xorList = []
        for index,binaryBitItem in enumerate(List):  # 同时访问数组下标 index
            if binaryBitItem[checkIndex] == 1:    # 4不能写死  若第n位为1，则hList中第2^(len(blist)-1-n)-1位为result
                if isinstance(hList[index],int):
                    xorList.append(hList[index])
                # print(binaryBitItem, hList[index])

        if len(xorList) == 1:
            result = xorList[0]
        elif len(xorList) >1:
            res = 0
            for item in xorList:
                res = res ^ item
        # print(res)
        indexInhList = (2 ** (bListLen-1-checkIndex))-1
        hList[indexInhList] = res

        # print("xorList::",xorList)
        checkIndex-=1

    print(hList)
    hammingCode = ''
    for it in hList:
        hammingCode+=str(it)
    print("海明码：",hammingCode)
    return hammingCode
    # print("List::::",List)

def main():
    hamming = input("请输入原码：")
    if(islegal(hamming)):
        toHamming(hamming)
    else:
        print("格式有误！")

if __name__ == '__main__':
    main()



