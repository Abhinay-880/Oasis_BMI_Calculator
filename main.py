# BMI CLACULATOR

# input

WEIGHT = int(input("Enter your weight in kilograms : "))

HEIGHT = int(input("Enter you height in meters : "))

# calculation

BMI = WEIGHT / (HEIGHT * HEIGHT)

print(f"Your BMI value is : {round(BMI,1)}")
# stages

if BMI < 18.5:
    print("YOU ARE UNDER WEIGHT,MAINTAIN PROPER DIET")
elif BMI > 18.5 and BMI < 25:
    print("YOU ARE NORMAL,CONTINUE YOUR DIET")
elif BMI > 25 and BMI < 30:
    print("YOU ARE OVER WEIGHT,MAINTAIN PROPER DIET")
else:
    print("YOUR ARE OBESE,YOU NEED TO CONSULT DOCTOR")
