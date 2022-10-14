weight = int(input("Enter your weight"))
height = float(input("Enter your height"))

height_sq = height*height
bmi = weight/height_sq

if bmi < 18.5:
    print("Underweight")
    
elif bmi >= 18.5 and  bmi < 25:
    print("Normal")
    
elif bmi >= 25 and bmi < 30:
    print("Overweight")
    
else:
    print("Obesity")
