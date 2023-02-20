# Initialize physics-test variables
train_mass = 22680
train_accel = 10
train_distance = 100
bomb_mass = 1


# Convert Celcius to Fahrenheit
def c_to_f(c_temp):
    f_temp = (c_temp * 9 / 5) + 32
    return f_temp

# Test
c0_in_fahrenheit = c_to_f(0)
print("\n0 degrees is", round(c0_in_fahrenheit, 1), "degrees Farenheit.")


# Convert Fahrenheit to Celcius
def f_to_c(f_temp):
    c_temp = (f_temp - 32) * (5 / 9)
    return c_temp

# Test
f100_in_celcius = f_to_c(100)
print("\n100 degrees is", round(f100_in_celcius, 1), "degrees Celcius.")


# Calculate force
def get_force(mass, acceleration):
    return mass * acceleration

# Test
train_force = get_force(train_mass, train_accel)
print("\nThe GE train supplies", train_force, "Newtons of force.")

# Calculate energy
def get_energy(mass, c = 3 * (10**8)):
  return mass * c**2

# Test
bomb_energy = get_energy(bomb_mass)
print("\nA 1kg bomb supplies", bomb_energy, "Joules.")


# Calculate work done using get_force
def get_work(mass, acceleration, distance):
  return get_force(mass, acceleration) * distance

# Test
train_work = get_work(train_mass, train_accel, train_distance)
print("\nThe GE train does", train_work, "Joules of work over", train_distance, "meters.")