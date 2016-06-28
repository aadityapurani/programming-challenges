#Day2 Operators
#Coded by Aaditya Purani
# Enter your code here. Read input from STDIN. Print output to STDOUT
mealCost = float(raw_input())
tipPercent = int(raw_input())
taxPercent = int(raw_input())

tip = mealCost * tipPercent/100
tax = mealCost * taxPercent/100
totalCost = mealCost + tip + tax
x = round(totalCost)
y = int(x)

print "The total meal cost is "+str(y)+" dollars."
