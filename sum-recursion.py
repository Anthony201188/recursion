## Write a recursive function to compute the sum of digits in a positive integer.


def sum_of_digits(n):
 if n == 1: #exit condition or "base case"
  return 1
 else:
  return n + sum_of_digits(n - 1)

# Testing the function
num = 10
result = sum_of_digits(num)
print(f"The sum of digits in {num} is {result}.") #--> 1 + 2 + 3 + 4 +5 +6 +7 +8+ 9 +10= ?