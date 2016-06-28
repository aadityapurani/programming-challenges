#Day 9 Recursion HackerRank
#Coded by Aaditya Purani
# Enter your code here. Read input from STDIN. Print output to STDOUT
num = int(raw_input().strip())
factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print factorial
