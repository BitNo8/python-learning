# 1. Test wether result of taking the power of one number to another number provides an answer which is greater than 5000

# Write your large_power function here:
def large_power(base, exponent):
    powered = base ** exponent
    if powered > 5000:
        print(powered)
        return True
    else:
        print(powered)
        return False

# Test----------------------

# should print True
print(large_power(2, 13))

# should print False
print(large_power(2, 12))

#-------------------------------------------------------------------------------

# 2. Our function will accept a parameter called budget which describes our spending limit. The next four parameters describe what we are spending our money on. We need to sum all of our spendings and compare it to the budget. If we have gone over budget, we will return True. Otherwise we return False.

# Write your over_budget function here:
def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
    sum = food_bill + electricity_bill + internet_bill + rent
    if sum > budget:
        print("We have gone over budget by $" + str(sum - budget) + "!!!")
        return True
    else:
        print("We're still under budget by $" + str(budget - sum) + "!")
        return False

# Test----------------------

# should print False
print(over_budget(100, 20, 30, 10, 40))

# should print True
print(over_budget(80, 20, 30, 10, 30))

#-------------------------------------------------------------------------------

# 3. In this challenge, we will determine if one number is twice as large as another number. To do this, we will compare the first number with two times the second number.

# Write your twice_as_large function here:
def twice_as_large(num1, num2):
    if num1 > num2 * 2:
        return True
    else:
        return False

# Test----------------------

# should print False
print(twice_as_large(10, 5))

# should print True
print(twice_as_large(11, 5))

#-------------------------------------------------------------------------------

# 4. To make things a bit more challenging, we are going to create a function that determines whether or not a number is divisible by ten. A number is divisible by ten if the remainder of the number divided by 10 is 0.

# Write your divisible_by_ten() function here:

def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False

# Test----------------------

# should print True
print(divisible_by_ten(20))

# should print False
print(divisible_by_ten(25))

#-------------------------------------------------------------------------------

# 5. Finally, we are going to check if the summation of two inputs does not equal ten. Our function will accept two inputs and add them together. If the two numbers added together are not equal to ten, then we will return True, otherwise, we will return False.

# Write your not_sum_to_ten function here:
  
def not_sum_to_ten(num1, num2):
  if num1 + num2 != 10:
    return True
  else:
    return False

# Test----------------------

# should print True
print(not_sum_to_ten(9, -1))

# should print False
print(not_sum_to_ten(9, 1))

# should print False
print(not_sum_to_ten(5,5))