

#JEDDY AWUOR ODUOR.
#SCT211 - 0027 / 20022.

print("Tip Calculator Assignment")

total_bill = int(input("Enter the total bill amount> "))
tip_percent = int(input("What percent would you like to tip?: 10 ,12 or 15 > "))
persons_splitting = int(input("How many people are splitting the bill?> "))

if tip_percent == 10:
    tip_amount = 0.1 * total_bill
    total_bill = (total_bill - tip_amount)
    one_bill = float(total_bill/persons_splitting)

if tip_percent == 12:
    tip_amount = 0.12 * total_bill
    total_bill = (total_bill-tip_amount)
    one_bill = float(total_bill/persons_splitting)

if tip_percent == 15:
    tip_amount = 0.15 * total_bill
    total_bill = (total_bill - tip_amount)
    one_bill = total_bill / persons_splitting

format_onebill = "{:.2f}".format(one_bill)

#one_bill = round(total_bill/persons_splitting, 2) --> rounds off to 2 d.p
#format_onebill = "{:.2f}".format(one_bill)-->does not round off just cuts to 2dp

# noinspection PyUnboundLocalVariable
print(f"Each person will be required to pay {format_onebill} , on the {total_bill} total bill ")