
#JEDDY AWUOR ODUOR, SCT211-0027/20022

print("BMI Calculator Assignment")

height = float(input("Enter your height in meters > "))
weight = float(input("Enter your weight in kg > "))

bmi = weight / (height ** 2)

format_bmi =  float("{:.2f}".format(bmi))

if format_bmi <= 18.50:
    print(f"Your bmi is : {format_bmi}. You are underweight.")

elif 18.50 < format_bmi <= 24.90:
    print(f"Your bmi is : {format_bmi}. You have a normal weight.")

elif 25.00 <= format_bmi <= 29.00:
    print(f"Your bmi is : {format_bmi}. You are  overweight.")

elif format_bmi >= 30.00:
    print(f"Your bmi is : {format_bmi}. You are  overweight.")

else:
    print("Invalid")


