

#JEDDY AWUOR ODUOR.
#SCT211 - 0027 / 20022.

print("Age Calculator Assignment")
current_year = 2023
current_month = 9
current_date = 30

birth_month = int(input("Enter your  birth month (integers)> "))
birth_date = int(input("Enter your  birth date(integers)> "))
birth_year = int(input("Enter your birth year(integers)> "))

expected_years = current_year-birth_year
expected_month = current_month-birth_month
expected_days = current_date-birth_date

if expected_days < 0:
    expected_month-= 1
    expected_days += 30

if expected_month < 0:
    expected_years -= 1
    expected_month += 12


print(f"You were born on {birth_month}/{birth_date}/{birth_year}")
print(f"Your current age will be {expected_years} years ,{expected_month} months and {expected_days} days")


