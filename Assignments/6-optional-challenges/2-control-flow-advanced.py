# 1. In Range: Let’s start the advanced challenge problems by testing if a number falls within a certain range. We will accept three parameters where the first parameter is the number we are testing, the second parameter is the lower bound and the third parameter is the upper bound of our range.

# Write your in_range function here:
def in_range(num1, num2, num3):
    if num1 >= num2 and num1 <= num3:
        return True
    else:
        return False

# Test----------------------

print(in_range(10, 10, 10))
# should print True
print(in_range(5, 10, 20))
# should print False

#-------------------------------------------------------------------------------

# 2. Same Name: We need to write a program that checks different names and determines if they are equal. We need to accept two strings and compare them.

# Write your same_name function here:

def same_name(your_name, my_name):
  if your_name == my_name:
    return True
  else:
    return False

# Test----------------------

print(same_name("Colby", "Colby"))
# should print True
print(same_name("Tina", "Amber"))
# should print False

#-------------------------------------------------------------------------------

# 3. Always False: There are some situations that you normally want to avoid when programming using conditional statements. One example is a contradiction. This occurs when your condition will always be false no matter what value you pass into it. Let’s create an example of a function that contains a contradiction.

# Write your always_false function here:

def always_false(num):
    if num > 0 and num < 0:
        return True
    else:
        return False

# Test----------------------

print(always_false(0))
# should print False
print(always_false(-1))
# should print False
print(always_false(1))
# should print False

#-------------------------------------------------------------------------------

# 4. Movie Review: We want to create a function that will help us rate movies. Our function will split the ratings into different ranges and tell the user how the movie was based on the movie’s rating.

# Write your movie_review function here:

def movie_review(rating):
    if rating <= 5:
        return "Avoid at all costs!"
    elif rating < 9:
        return "This one was fun."
    else:
        return "Outstanding!"

# Test----------------------

print(movie_review(9))
# should print "Outstanding!"
print(movie_review(4))
# should print "Avoid at all costs!"
print(movie_review(6))
# should print "This one was fun."

#-------------------------------------------------------------------------------

# 5. Max Number: For the final challenge, we are going to select which number from three input values is the greatest using conditional statements. To do this, we need to check the different combinations of values to see which number is greater than the other two.

# Write your max_num function here:

def max_num(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    elif num3 > num1 and num3> num2:
        return num3
    else:
        return "It's a tie!"

# Test----------------------

print(max_num(-10, 0, 10))
# should print 10
print(max_num(-10, 5, -30))
# should print 5
print(max_num(-5, -10, -10))
# should print -5
print(max_num(2, 3, 3))
# should print "It's a tie!"
