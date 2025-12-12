#Exercise3
#Calculate BMI for people 16years and older

#Display tille and instructions 
print ("==========BMI calculator==========")
print ("Please enter your weight and height")

#User inputs 
weight = float(input("Enter your weight in kilograms:"))
height = float(input("Enter your height in meters:"))

#Formula for calculating BMI
bmi = weight / (height ** 2)

#Conditions for BMI categories
if bmi < 18.5:
    print("Your BMI is:", round(bmi,2), "Underweight")
elif 18.5 <= bmi <= 24.9:
    print("Your BMI is:", round(bmi,2), "Normal ")
elif 25 <= bmi <= 29.9:
    print("Your BMI is:", round(bmi,2), "Overweight")
else:
    print("Your BMI is:", round(bmi,2), "Obese")
    