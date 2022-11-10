def name_digit():
    num = int(input( "Enter a number between 0-9 : "))
    num_digits = ("zero", "One", "Two", "Three", "Four", "Five",
                  "six", "Seven", "Eight", "Nine")
    print (f"The name of digit {num} is {num_digits[num]}")
    

name_digit()
