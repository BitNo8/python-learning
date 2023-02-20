weight = input("What is the package weight? \n")
weight = float(weight)
print(weight,"\n")

#Ground Shipping
def groundShip():
  if weight > 10:
    print("It costs $" + str(((4.75 * weight) + 20)) + " to ship via Ground")
  elif weight > 6:
    print("It costs $" + str(((4.00 * weight) + 20)) + " to ship via Ground")
  elif weight > 2:
    print("It costs $" + str(((3.00 * weight) + 20)) + " to ship via Ground")
  else:
    print("It costs $" + str(((1.50 * weight) + 20)) + " to ship via Ground")

def groundShipPremium():
    print("It costs $" + str(125) + " to ship via Ground Premium")

def droneShip():
  if weight > 10:
    print("It costs $" + str((14.25 * weight)) + " to ship via Drone")
  elif weight > 6:
    print("It costs $" + str((12.00 * weight)) + " to ship via Drone")
  elif weight > 2:
    print("It costs $" + str((9.00 * weight)) + " to ship via Drone")
  else:
    print("It costs $" + str((4.50 * weight)) + " to ship via Drone")