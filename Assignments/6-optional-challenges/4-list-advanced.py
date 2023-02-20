# 1. Every Three Numbers
def every_three_nums(start):
  return list(range(start, 101, 3))

# Uncomment the line below when your function is done
print(every_three_nums(91))

#-------------------------------------------------------------------------------

# 2. Remove Middle
def remove_middle(my_list, start, end):
    # To make this problem easier, we can use slicing. For example, if we wanted all elements up to a certain index we can use my_list[:index] and to get all elements after a certain index we can use my_list[index+1:].
    return my_list[:start] + my_list[end+1:]

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))