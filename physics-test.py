#Initialize train variables
train_mass = 22680
train_accel = 10
train_distance = 100

#Initialize bomb variable
bomb_mass = 1

#Function: Convert Farenheit to Celcius
def f_to_c(f_temp):
    c_temp = (f_temp - 32) * (5/9)
    return c_temp

#Test f_to_c
#f100_in_celcius = f_to_c(100)
#print("100 degrees is",round(f100_in_celcius, 1), "degrees Celcius.")