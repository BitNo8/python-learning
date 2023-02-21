# 1. Larger Sum: We are going to start our advanced challenge problems by calculating which list of two inputs has the larger sum. We will iterate through each of the list and calculate the sums, afterwards we will compare the two and return which one has a greater sum.

#Write your function here
def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for num in lst1:
    sum1 += num
  for num in lst2:
    sum2 += num
  if sum1 >= sum2:
    return lst1
  else:
    return lst2

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))

#-------------------------------------------------------------------------------

# 2. Over 9000: We are constructing a device that is able to measure the power level of our coding abilities and according to the device, it will be impossible for our power levels to be over 9000. Because of this, as we iterate through a list of power values we will count up each of the numbers until our sum reaches a value greater than 9000. Once this happens, we should stop adding the numbers and return the value where we stopped.

#Write your function here
def over_nine_thousand(lst):
    sum = 0
    for num in lst:
      sum += num
      if sum > 9000:
          break
    return sum

#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))

#-------------------------------------------------------------------------------

# 3. Max Num: Here is a more traditional coding problem for you. This function will be used to find the maximum number in a list of numbers. This can be accomplished using the max() function in python, but as a challenge, we are going to manually implement this function.

#Write your function here
def max_num(nums):
  max = nums[0]
  for num in nums:
    if num > max:
      max = num
  return max

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))

#-------------------------------------------------------------------------------

# 4. Same Values: In this challenge, we need to find the indices in two equally sized lists where the numbers match. We will be iterating through both of them at the same time and comparing the values, if the numbers are equal, then we record the index.

#Write your function here
def same_values(lst1, lst2):
  new_lst = []
  for i in range(len(lst1)):
    if lst1[i] == lst2[i]:
      new_lst.append(i)
  return new_lst

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

#-------------------------------------------------------------------------------

# 5. Reversed List: For the final challenge, we are going to test two lists to see if the second list is the reverse of the first list. There are a few different ways to approach this, but we are going to try a method that iterates through each of the values in one direction for the first list and compares them against the values starting from the other direction in the second list.

# In this code, we iterate through each of the indices for the entire length of either of the lists (since we assume the lengths are equal) and we perform a comparison on each of the elements. We get the element at the current index from our first list with lst1[index] and we test it against the last index of the second list minus the current index len(lst2) - 1 – index.

# That math is a little complicated — it helps to look at a concrete example. If we are given a list of 5 elements, the valid indices are 0 to 4. Because of this, the last index in the second list is len(lst2) - 1, or 5 - 1 = 4. Now in order to get the inverse of the position we are at in the first list, we subtract the index we are at from the end of the second list. So on the first pass, we’ll compare the element at position 0 to the element at position 5 - 1 - 0 = 4. On the next pass, we’ll compare the element at position 1 to the element at position 5 - 1 - 1 = 3, and so on.

# If any of the two elements are not equal then we know that the second list is not the reverse of the first list and we return False. If we made it to the end without a mismatch then we can return True since the second list is the reverse of the first. You could also try simplifying this code by using the python function reversed() or other methods that you will learn later on such as ‘slicing’.

#Write your function here
def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True

# Alternate Answer:
#def reversed_list(lst1, lst2):
#for i in range(len(lst1)):
#if lst1[i] == lst2[-1 - i]:
#    continue
#else:
#    return False
#return True

#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))