def bmi():
    height = float(input("Enter your height in meters: "))
    weight = float(input("Enter your weight in kilograms: "))
    bmi_value = weight / (height ** 2)
    print(f"Your BMI is: {bmi_value:.2f}")
    if bmi_value < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi_value < 24.9:
        print("You have a normal weight.")
    elif 25 <= bmi_value < 29.9:
        print("You are overweight.")
    else:
        print("You are obese.")
bmi()