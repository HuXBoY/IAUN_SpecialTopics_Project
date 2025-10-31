while 1:
    base_number = int(input("Enter a 2 digit number: "))

    if base_number > 9 and base_number < 100:
        first_digit = base_number // 10
        second_digit = base_number % 10
        print("[1st digit]^[2nd digit]: ", first_digit ** second_digit)
        print("[2nd digit]^[1st digit]: ", second_digit ** first_digit)
    else:
        print("Not a 2 digit number")
