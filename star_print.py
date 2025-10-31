while 1:
    lines = int(input("Enter the number of lines: ")) + 1

    for i in range(lines):
        for j in range(i):
            print("*", end="")
        print()
