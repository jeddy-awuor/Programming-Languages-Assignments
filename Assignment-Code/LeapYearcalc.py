# JEDDY AWUOR ODUOR, SCT211-0027/20022

print("Leap Year Calculator Assignment")


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap Year")
    else:
        print("Not a leap year")


year = int(input("Enter a year: "))

is_leap_year(year)  # calling the function for checking if a yearis leap or not
