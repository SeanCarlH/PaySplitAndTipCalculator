#This is a calculator that allows you to determine the cost of you bill (including tip)
#when split between mutiple people

print("Welcome to the Tip Calculator!\n")
total = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people are splitting this bill? "))

percent = tip / 100
final_total = total + (percent * total)
pay_result = round(final_total / people, 2)
final_pay_result = "{:.2f}".format(pay_result)
print(f"Each person should pay ${final_pay_result}")