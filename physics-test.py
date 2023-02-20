# Initialize physics-test variables
train_mass = 22680
train_accel = 10
train_distance = 100
bomb_mass = 1


# Convert Celcius to Farenheight
def c_to_f(c_temp):
    f_temp = (c_temp * 9 / 5) + 32
    return f_temp

# Test
c0_in_farenheit = c_to_f(0)
print("\n0 degrees is", round(c0_in_farenheit, 1), "degrees Farenheight.")


# Convert Fahrenheit to Celcius
def f_to_c(f_temp):
    c_temp = (f_temp - 32) * (5 / 9)
    return c_temp

# Test
f100_in_celcius = f_to_c(100)
print("\n100 degrees is", round(f100_in_celcius, 1), "degrees Celcius.")


# Calculate Force
def get_force(mass, acceleration):
    return mass * acceleration

# Test
train_force = get_force(train_mass, train_accel)
print("\nThe GE train supplies", train_force, "Newtons of force.")
