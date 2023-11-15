class AgeCalculator:
    def __init__(self, current_year, current_month, current_day):
        self.current_year = current_year
        self.current_month = current_month
        self.current_day = current_day

    def calculate_age(self, birth_year, birth_month, birth_day):
        age = self.current_year - birth_year - ((self.current_month, self.current_day) < (birth_month, birth_day))
        print(f"You were born on  {birth_year}-{birth_month}-{birth_day}.")
        return age


age_calculator = AgeCalculator(2023, 11, 4)

age = age_calculator.calculate_age(2003, 12, 6)

print(f"You are therefore {age} years old.")
