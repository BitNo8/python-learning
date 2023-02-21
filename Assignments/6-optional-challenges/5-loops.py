# 1. Divisible by Ten: Let’s start our code challenges with a function that counts how many numbers are divisible by ten from a list of numbers. This function will accept a list of numbers as an input parameter and use a loop to check each of the numbers in the list. Every time a number is divisible by 10, a counter will be incremented and the final count will be returned.

def divisible_by_ten(nums):
  counter = 0
  for num in nums:
    if num % 10 == 0:
      counter += 1
  return counter

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))

#-------------------------------------------------------------------------------
# 2. Greetings Loop: Let’s start our code challenges with a function that counts how many numbers are divisible by ten from a list of numbers. This function will accept a list of numbers as an input parameter and use a loop to check each of the numbers in the list. Every time a number is divisible by 10, a counter will be incremented and the final count will be returned.

def add_greetings(names):
  greetings = []
  for name in names:
    greetings.append("Hello, " + name)
  return greetings

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))

#-------------------------------------------------------------------------------

# 3. Delete Starting Evens: Let’s try a tricky challenge involving removing elements from a list. This function will repeatedly remove the first element of a list until it finds an odd number or runs out of elements. It will accept a list of numbers as an input parameter and return the modified list where any even numbers at the beginning of the list are removed.

#Write your function here
def delete_starting_evens(lst):
  while len(lst) > 0 and lst[0] % 2 == 0:
    lst = lst[1:]
  return lst

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

#-------------------------------------------------------------------------------

# 4. Odd Indices: Create a function named odd_indices() that has one parameter named lst. The function should create a new empty list and add every element from lst that has an odd index. The function should then return this new list.

#Write your function here
def odd_indices(lst):
  new_lst = []
  for i in range(1,len(lst), 2):
    new_lst.append(lst[i])
  return new_lst

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))