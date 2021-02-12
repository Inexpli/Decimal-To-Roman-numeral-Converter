x = input("Enter numbers from 1 - 100: ")
liczby1 = []
liczby2 = []

if len(str(x)) == 1:
    if int(x) == 1:
        print("I")
    elif int(x) == 2:
        print("II")
    elif int(x) == 3:
        print("III")
    elif int(x) == 4:
        print("IV")
    elif int(x) == 5:
        print("V")
    elif int(x) == 6:
        print("VI")
    elif int(x) == 7:
        print("VII")
    elif int(x) == 8:
        print("VIII")
    elif int(x) == 9:
        print("IX")
    else:
        print("An invalid number has been entered, the range is 1-100")

elif len(str(x)) == 2:
    for i in str(x):
        liczby1.append(int(i))


    def drugieliczby():
        if liczby1[1] == 0:
            liczby2.append("")
        elif liczby1[1] == 1:
            liczby2.append("I")
        elif liczby1[1] == 2:
            liczby2.append("II")
        elif liczby1[1] == 3:
            liczby2.append("III")
        elif liczby1[1] == 4:
            liczby2.append("IV")
        elif liczby1[1] == 5:
            liczby2.append("V")
        elif liczby1[1] == 6:
            liczby2.append("VI")
        elif liczby1[1] == 7:
            liczby2.append("VII")
        elif liczby1[1] == 8:
            liczby2.append("VIII")
        else:
            liczby2.append("IX")


    if liczby1[0] == 1:
        liczby2.append("X")
        drugieliczby()
    elif liczby1[0] == 2:
        liczby2.append("XX")
        drugieliczby()
    elif liczby1[0] == 3:
        liczby2.append("XXX")
        drugieliczby()
    elif liczby1[0] == 4:
        liczby2.append("XL")
        drugieliczby()
    elif liczby1[0] == 5:
        liczby2.append("L")
        drugieliczby()
    elif liczby1[0] == 6:
        liczby2.append("LX")
        drugieliczby()
    elif liczby1[0] == 7:
        liczby2.append("LXX")
        drugieliczby()
    elif liczby1[0] == 8:
        liczby2.append("LXXX")
        drugieliczby()
    elif liczby1[0] == 9:
        liczby2.append("XC")
        drugieliczby()

    print(liczby2[0] + liczby2[1])

elif int(x) == 100:
    print("C")

else:
    print("An invalid number has been entered, the range is 1-100")
