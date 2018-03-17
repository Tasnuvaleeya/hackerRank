def timeConversion(s):
    # Complete this function
    # print(s[-2:])
    # return int(s[:2])+ 12
    if s[-2:] == 'PM':
        if s[0:2] == '12':
            return s[:-2]
        else:
            return str(int(s[0:2])+12) + str(s[2:-2])
    else:
        if s[-2:] == 'AM':
            if s[0:2] == '12':
                res = str(s[:2]).replace('12','00') + s[2:-2]
                return res

            else:
                return s[:-2]


s = input().strip()
result = timeConversion(s)
print(result)
