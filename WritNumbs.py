num = int(input("A number between 1 and 99."))


tens = num // 10 #First Numb
ones = num % 10 #Second Numb
if tens == 9:
    print("ninety")
if tens == 8:
    print("Eighty")
if tens == 7:
        print("Seventy")
if tens == 6:
        print("Sixty")
if tens == 5:
        print("Fifty")
if tens == 4:
        print("Fourty")
if tens == 3:
    print("Thirty")
if tens == 2:
    print("Twenty")

if ones == 1:
    if tens == 1:
        print(" Eleven ")
    else:
        print( "Ten ")

if ones == 2:
    if tens == 1:
        print("Twelve")
    else:
        print(" two")

if ones == 3:
    if tens == 1:
        print("Thirteen")
    else:
            print(" three")

if ones == 4:
    if tens == 1:
        print("Fourteen")
    else:
            print(" four")

if ones == 5:
    if tens == 1:
        print("Fifteen")
    else:
            print(" five")

if ones == 6:
    if tens == 1:
        print("Sixteen")
    else:
            print(" six ")

if ones == 7:
    if tens == 1:
        print("Seventeen")
    else:
            print(" seven")

if ones == 8:
    if tens == 1:
        print("Eightteen")
    else:
        print(" eight")

if ones == 9:
    if tens == 1:
        print("Nineteen")
    else:
        print(" nine")
