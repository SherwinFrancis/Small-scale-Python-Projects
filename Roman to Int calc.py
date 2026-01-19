def romanToInt(s) :
    key =  {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }
    total = 0

    for i in range(0, len(s)):
        if (i < len(s) - 1) and key[s[i]] < key[s[i+1]]:
            total -= key[s[i]]
        else:
            total += key[s[i]]

    return total 

print(romanToInt("XCIV"))




    


        