def romanMap():
    map=(("M",  1000),("CM", 900),("D",  500),("CD", 400),("C",  100),("XC", 90),("L",  50),("XL", 40),("X",  10),("IX", 9),("V",  5),("V", 4),("I",  1))
    return map
firstNum=ns([0])
secondNum=ns([1])
def main():
    ns=str(input("Enter a roman numeral"))
    total=0
    result=0
    while ns:
        firstNum=(romanMap(ns[0]))
         secondNum=(romanMap(ns[1]) 
        if firstNum is len(ns)>1 or secondNum-1:
                        total=total+firstNum
            ns=ns[1:]
        else:
                        total=total+ns[1]-ns[0]
            ns=ns[2:]
      print (total)
main()
