#
num = int(input("A number between 1 and 99."))

tens = num // 10
ones = num % 10

def get_tens(tens):
    if tens == 0:
        tens_number = ""
    if tens == 1:
        tens_number = ""
    if tens == 9:
        tens_number = "ninety"
    if tens == 8:
        tens_number = "Eighty"
    if tens == 7:
        tens_number = "Seventy"
    if tens == 6:
        tens_number = "Sixty"
    if tens == 5:
        tens_number = "Fifty"
    if tens == 4:
        tens_number = "Fourty"
    if tens == 3:
        tens_number = "Thirty"
    if tens == 2:
        tens_number = "Twenty"
    return tens_number

def get_ones(ones , tens):
    if ones == 1:
        if tens == 1:
            ones_number = " Eleven "
        else:
            ones_number =  "Ten "

    if ones == 2:
        if tens == 1:
            ones_number = "Twelve"
        else:
            ones_number = " two"

    if ones == 3:
        if tens == 1:
            ones_number = "Thirteen"
        else:
            ones_number = " three"

    if ones == 4:
        if tens == 1:
            ones_number = "Fourteen"
        else:
            ones_number = " four"

    if ones == 5:
        if tens == 1:
            ones_number = "Fifteen"
        else:
            ones_number = " five"

    if ones == 6:
        if tens == 1:
            ones_number = "Sixteen"
        else:
            ones_number = " six "

    if ones == 7:
        if tens == 1:
            ones_number = "Seventeen"
        else:
            ones_number = " seven"

    if ones == 8:
        if tens == 1:
            ones_number = "Eightteen"
        else:
            ones_number = " eight"

    if ones == 9:
        if tens == 1:
            ones_number = "Nineteen"
        else:
            ones_number = " nine"
    return ones_number


def main():
    tens_number = get_tens(tens)
    ones_number = get_ones(ones , tens)

    return print(tens_number , ones_number )

main()
