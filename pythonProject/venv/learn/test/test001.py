def romanToInt(s):
    dic = {
        'I': 1, 'IV': 4, 'V': 5, 'IX': 9,
        'X': 10, 'XL': 40, 'L': 50, 'XC': 90,
        'C': 100, 'CD': 400, 'D': 500, 'CM': 900,
        'M': 1000
    }
    i=0
    res=0
    while i<len(s):
        if len(s)==1:
            return dic[s]
        if s[i:i+2] in dic:
            res+=dic[s[i:i+2]]
            i+=2
        else:
            res+=dic[s[i]]
            i+=1
    return res

if __name__ == '__main__':
    c=romanToInt('CDXC')
    print(c)

