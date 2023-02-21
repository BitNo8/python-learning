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

# 4.

# 5.