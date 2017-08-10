num = int(input("A number between 1 and 99."))


tens = num // 10 #First Numb
ones = num % 10 #Second Numb
if tens == 9:
    tens_word = "ninety"
elif tens == 8:
    tens_word = "Eighty"
elif tens == 7:
    tens_word == "Seventy"
elif tens == 6:
    tens_word == "Sixty"
elif tens == 5:
    tens_word == "Fifty"
elif tens == 4:
    tens_word == "Fourty"
elif tens == 3:
    tens_word == "Thirty"
elif tens == 2:
    tens_word == "Twenty"
