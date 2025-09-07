while True:
    i = float(input("Enter length in inches:"))
    if i < 0:
        print("Program ended.")
        break
    cm = i * 2.54
    print(f"{i} inches = {cm} cm\n")
