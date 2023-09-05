#BMI calculator
print("Welcome to the BMI Calculator.")
height = float(input("Enter your height in m : "))
weight = float(input("Enter your weight in kg: "))
BMI = weight / (height ** 2)
print(f"Your BMI is: {round(BMI)}")
