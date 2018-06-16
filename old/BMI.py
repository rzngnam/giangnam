weight = float(input("weight(kg) ?"))
height = float(input("height(m) ?"))

bmi = weight/height**2

if bmi < 16:
    print("Severely underweight")
elif bmi <= 18.5:
    print("underweight")
elif bmi <= 25:
    print("normal")
elif bmi <= 30:
    print("overweight")
else:
    print("obese")



