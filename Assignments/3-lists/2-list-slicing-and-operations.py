# Your code below:
#Separate 1D Arrays
toppings = ["pepperoni", "pineapple", "chesse", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

#Counting $2 slices and total number of pizzas offered
num_two_dollar_slices = prices.count(2)
num_pizzas = (len(toppings))

#Promoting our variety of flavors!
print("We sell", num_pizzas, "different kinds of pizza!")

#Constructing 2D Array of Pizza/Prices
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
print(pizza_and_prices)

#Sorting by ascending price order
pizza_and_prices.sort()
print("\n")
print(pizza_and_prices)

#Storing/Printing cheapest pizza after sort
cheapest_pizza = pizza_and_prices[0]
print("\n")
print(cheapest_pizza)

#Storing/Printing priciest pizza after sort
priciest_pizza = pizza_and_prices[-1]
print("\n")
print(priciest_pizza)

#Removing priciest pizza (without a parameter it removes the last index)
pizza_and_prices.pop()
print("\n")
print(pizza_and_prices)

#Adding new pizza flavor
pizza_and_prices.insert(4, [2.5, "peppers"])
print("\n")
print(pizza_and_prices)

#Storing three cheapest pizzas
three_cheapest = pizza_and_prices[:3]
print("\n")
print(three_cheapest)