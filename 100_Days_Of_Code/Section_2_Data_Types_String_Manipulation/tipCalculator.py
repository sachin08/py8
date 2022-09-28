print("Welcome to the tip calculator!")
totalBill = float(input("What was the total bill? $"))
noOfPeople = int(input("How many people to split the bill? "))
tipPercent = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

amountCal = totalBill + (totalBill * (tipPercent/100))
finalAmountPerPerson = round((amountCal/noOfPeople),2)
print(f"Each person should pay: ${finalAmountPerPerson}")
