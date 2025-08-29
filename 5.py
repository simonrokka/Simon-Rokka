mass1 = float(input("Enter a mass in talents: "))
mass2 = float(input("Enter a mass pounds: "))
mass3 = float(input("Enter a mass lots: "))
total_grams = (mass1 * 20 * 32 * 13.3) + (mass2 * 32 * 13.3) + (mass3 * 13.3)
kg = total_grams // 1000
gm = total_grams % 1000
print(f"the mass in modern system is {kg}kg and {gm}g")