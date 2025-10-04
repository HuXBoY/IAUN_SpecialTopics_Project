while 1:
    op = input("Select operation ( + - * / ** ) or type anything else to quit: ")
    if op != "+" and op != "-" and op != "*" and op != "/" and op != "**":
        print("Quitting.")
        break

    first_number = int(input("Type First Number: "))
    second_number = int(input("Type Second Number: "))

    if op == "+":
        print(first_number + second_number)

    elif op == "-":
        print(first_number - second_number)

    elif op == "*":
        print(first_number * second_number)

    elif op == "/":
        print(first_number / second_number)

    else:
        print(first_number ** second_number)