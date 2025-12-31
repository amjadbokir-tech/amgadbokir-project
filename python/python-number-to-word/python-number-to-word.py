
#database.
ones = {

    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}

tens = {
    10: "ten",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}

elevns = {
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}

hundred = {
    100: "one hundred",
    200: "two hundred",
    300: "three hundred",
    400: "four hundred",
    500: "five hundred",
    600: "six hundred",
    700: "seven hundred",
    800: "eight hundred",
    900: "nine hundred"
}

#opreating_function.
def oness(num):
    return ones[num]

def tenss(num):
    return tens[num]

def elevens(num):
    return elevns[num]

def tens_column(num):
    str_num = str(num)
    strnum = str_num[0] + "0"
    num_int = int(strnum)
    return tens[num_int]

def ones_column(num):
    str_num = str(num)
    strnum = str_num[1]
    num_int = int(strnum)
    return ones[num_int]


def ones_columns(num):
    str_num = str(num)
    strnum = str_num[2]
    num_int = int(strnum)
    return ones[num_int]


def hundreds_column(num):
    str_num = str(num)
    strnum = str_num[0] + "00"
    num_int = int(strnum)
    return hundred[num_int]

def minus_hundreds(num):
    str_num = str(num)
    strnum = str_num[1:]
    num_int = int(strnum)
    return num_int



#main_function.

def main():
     number = int(input("Enter a number:"))
     str_num = str(number)
     if len(str_num) == 1:#every len == 1 here
            print(ones[number])
     elif len(str_num) == 2:#every len == 2 here
         if str_num[1] == "0":
             print(tens[number])
         elif str_num[0] == "1":
             print(elevns[number])
         elif str_num[1] != "0" and str_num[0] != "1":
             print(tens_column(number) + "-" + ones_column(number))
     elif len(str_num) == 3:#every len == 3 here
         if str_num[1] == "0" and str_num[2] == "0":
             print(hundred[number])
         elif str_num[1] != "0" and str_num[2] == "0":
             print(hundreds_column(number) + " and " + tens[minus_hundreds(number)])
         elif str_num[1] == "1" :
             print(hundreds_column(number) + " and " + elevns[minus_hundreds(number)])
         elif str_num[1] == "0" and str_num[2] != "0":
             print(hundreds_column(number) + " and " + ones_columns(number))
         elif str_num[1] != "0" and str_num[2] != "0":
             print(hundreds_column(number) + " and " + tens_column(minus_hundreds(number)) + "-" + ones_column(minus_hundreds(number)))









choice = input("press enter to continue or q to quit: ")
while choice != "q":
    main()
    if choice == "q":
        break



