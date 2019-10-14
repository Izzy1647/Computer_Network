def islegal(string):
    return string.count('1') + string.count('0') == len(string)


def change(n):  # 十进制转二进制
    result = '0'
    if n == 0:  # 输入为0的情况
        return result
    else:
        result = change(n // 2)  # 调用自身
        return result + str(n % 2)


def smallest_check_number(k):
    r = 1
    while 2 ** r - r - 1 < k:
        r += 1  # 得到最小检测位数
    return r

def toHamming(hammingList):

    hList = []
    for i in str(hammingList):
        hList.append(int(i))  # 转换为列表

    # print(smallest_check_number(len(hList)))
    for j in range(smallest_check_number(len(hList))):  # 插入海明检验码的位置
        hList.insert(2 ** j - 1, "a" + str(2 ** j - 1))
    print("hList:", hList)

    List = []
    for a in range(len(hList)):
        b = change(a + 1).zfill(int(len(hList)))  # 不足补零
        # print("b",b)
        blist = []
        for i in str(b):
            blist.append(int(i))
        List.append(blist)
        print("blist" + str(a), blist)

    xorList = []
    for i in range(len(hList)-1):
      for index, binaryBitItem in enumerate(List):  # 同时访问数组下标 index
          if binaryBitItem[len(blist)-1-i] == 1:  # 4不能写死  若第n位为1，则hList中第2^(len(blist)-1-n)-1为result
            if isinstance(hList[index], int):
                xorList.append(hList[index])
            # print(binaryBitItem, hList[index])
      # print("xorList"+str(i)+":", xorList)
      result = 0
      for c in xorList:
        result = result ^ c
      # print(result)
      if((hList[i]!=0)&(hList[i]!=1)):
        hList[i]=result
      xorList = []
    # print("List::::", List)
    resstr = ''
    for s in hList:
        resstr += str(s)
    print("海明码：",resstr)
    return resstr


def main():
    hammingCode = input("请输入原码：")
    if(islegal(hammingCode)):
        toHamming(hammingCode)
    else:
        print("Not legal input.")

if __name__ == '__main__':
    main()

# data = input("Input the data in bytes:")
#
# if(islegal(data)):
#     print("legal input.")
# else:
#     print("not legal!!")