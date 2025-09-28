import sys

if __name__ == "__main__":
    try:
        with open(sys.argv[1], "rb") as f:
            data = f.read()
    except:
        print("Failed to open file %s" % sys.argv[1])
        exit()
    line = "\""
    escaped = False
    for c in data:
        # \ 和 " 需要转义 
        if c == ord('\\'): 
            line += "\\\\"
        elif c == ord('\"'): 
            line += "\\\""
        # 如果是ASCII字符
        elif c >= 33 and c <= 126: 
            # 如果前一个是八进制转义字符, 后一个是0-7数字的话则也需要转八进制
            if escaped == True and c >= ord('0') and c <= ord('7'): 
                line += "\\%o" % c
            # 否则可以直接输出
            else: 
                line += "%c" % c
                escaped = False
        # 非ASCII字符转为八进制
        else: 
            line += "\\%o" % c 
            escaped = True
        # 输出一行, 长度控制在80列以内
        if len(line) > 75: 
            print(line + "\"")
            line = "\""
            escaped = False
    print(line + "\"")
