num = []
while True:
    give_num = input("Enter a number:")
    if give_num == "":
        print("Program ended.")
        break
    nums = float(give_num)
    num.append(nums)
    print(sorted(num))
    print(sorted(num, reverse=True))