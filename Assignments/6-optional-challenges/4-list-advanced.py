# 1. Every Three Numbers: Let’s start our challenging problems with a function that creates a list of numbers up to 100 in increments of 3 starting from a number that is passed to the function as an input parameter.

def every_three_nums(start):
  return list(range(start, 101, 3))

# Uncomment the line below when your function is done
print(every_three_nums(91))

#-------------------------------------------------------------------------------
# 2. Remove Middle: Our next function will remove all elements from a list with an index within a certain range. The function will accept a list, a starting index, and an ending index. All elements with an index between the starting and ending index should be removed from the list.

def remove_middle(my_list, start, end):
    # To make this problem easier, we can use slicing. For example, if we wanted all elements up to a certain index we can use my_list[:index] and to get all elements after a certain index we can use my_list[index+1:].
    return my_list[:start] + my_list[end+1:]

# Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

#-------------------------------------------------------------------------------
# 3. More Frequent Item: Let’s go back to our factory example. We have a conveyor belt of items where each item is represented by a different number. We want to know, out of two items, which one shows up more on our belt. To solve this, we can use a function with three parameters. One parameter for the list of items, another for the first item we are comparing, and another for the second item.

def more_frequent_item(my_list, item1, item2):
  if my_list.count(item1) >= my_list.count(item2):
    return item1
  else:
    return item2
# Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

#-------------------------------------------------------------------------------
# 4. Double Index: Our next function will double a value at a given position. We will provide a list and an index to double. This will create a new list by replacing the value at the index provided with double the original value. If the index is invalid then we should return the original list.

def double_index(my_list, index):
  # Checks to see if index is too big
  if index >= len(my_list):
    return my_list
  else:
    # Gets the original list up to index
    my_new_list = my_list[0:index]
 # Adds double the value at index to the new list 
  my_new_list.append(my_list[index]*2)
  #  Adds the rest of the original list
  my_new_list = my_new_list + my_list[index+1:]
  return my_new_list

# Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))

#-------------------------------------------------------------------------------
# 5. Middle Element: For the final code challenge, we are going to create a function that finds the middle item from a list of values. This will be different depending on whether there are an odd or even number of values. In the case of an odd number of elements, we want this function to return the exact middle value. If there is an even number of elements, it returns the average of the middle two elements.

def middle_element(my_list):
    #Check if list length is odd or even
  if len(my_list) % 2 == 0:
    sum = my_list[int(len(my_list)/2)] + my_list[int(len(my_list)/2) - 1]
    return sum / 2
  else:
    return my_list[int(len(my_list)/2)]

# Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5,]))