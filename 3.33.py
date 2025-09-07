sex = input("input enter your gender:")
hemo_value = float(input("enter your hemoglobin value:"))
if (sex == "Male"):
    if (134 <= hemo_value <= 167):
        print("your hemoglobin value is normal")
    elif (hemo_value < 134):
        print("your hemoglobin value is low")
    else:
        print("your hemoglobin value is high")
elif (sex == "Female"):
    if (117 <= hemo_value <= 155):
        print("your hemoglobin value is normal")
    elif (hemo_value < 117):
        print("your hemoglobin value is low")
    else:
        print("your hemoglobin value is high")
