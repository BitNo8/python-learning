#Initialize train variables
train_mass = 22680
train_accel = 10
train_distance = 100

#Initialize bomb variable
bomb_mass = 1

#Function: Convert Celcius to Farenheight
def c_to_f(c_temp):
    f_temp = (c_temp * 9/5) + 32
    return f_temp

#Testing c_to_f
#c0_in_farenheit = c_to_f(0)
#print("0 degrees is",round(c0_in_farenheit, 1), "degrees Farenheight.")