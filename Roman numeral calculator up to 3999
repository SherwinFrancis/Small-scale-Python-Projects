n = int(input(" Please enter a number between 1 and 3999"))
def solution(n):
    oneth = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
    tenth = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
    hundredth = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
    thousandth = ["","M","MM","MMM"]
    thousandPlace = n // 1000
    hundredPlace = (n % 1000) // 100
    tenPlace = (n % 1000) % 100 // 10
    onePlace = ((n % 1000) % 100) % 10 
    romanNumeral = thousandth[thousandPlace]
    romanNumeral += hundredth[hundredPlace]
    romanNumeral += tenth[tenPlace]
    romanNumeral += oneth[onePlace]
    return romanNumeral

print(solution(n))
