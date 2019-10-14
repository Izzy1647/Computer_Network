def XOR(str1, str2):  # 两字符串异或 模2运算
    res = ''
    if str1[0] == '0':
        return '0', str1[1:]
    else:
        for i in range(len(str1)):
            if str1[i] == '0' and str2[i] == '0':
                res = res + '0'
            elif str1[i] == '1' and str2[i] == '1':
                res = res + '0'
            else:
                res = res + '1'
    # print("result:",res[1:])
    return '1', res[1:]


def toCRC(data, rule):
    length = len(rule)
    data2 = data + '0' * (length - 1)   # 补0

    res = ''
    temp = data2[0:length]
    for i in range(len(data)):
        str, temp = XOR(temp, rule)
        res += str
        if i == len(data) - 1:
            break
        else:
            temp += data2[i + length]
    res = data + temp
    return res


def islegal(string):
    return string.count('1')+string.count('0') == len(string)

def main():  # 主函数

    rawData = input("输入原始数据：")
    rule = input("生成规则：")
    if islegal(rawData) and islegal(rule):
        print("crc：",toCRC(rawData,rule))
    else:
        print("illegal input.")

if __name__ == '__main__':
    main()
