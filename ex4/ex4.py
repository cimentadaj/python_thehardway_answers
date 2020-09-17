# There are 100 cars
cars = 100

# There are 4 slots in each car. This should be an integer!
space_in_a_car = 4.0

# There are 30 drivers
drivers = 30

# There are 90 passengers
passengers = 90

# The number of cars not drive is just the number of cars - the number of
# drivers
cars_not_driven = cars - drivers

# The number of cars driven is just the number of drivers
cars_driven = drivers

# carpool capacity is the number of 'empty' slots
carpool_capacity = cars_driven * space_in_a_car

# average passenger per car is the number of empty seats
average_passenger_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passenger_per_car, "in each car.")


# Study drill

# 0.
# The error  means that the variable car_pool_capacity is not define. He
# got confused and wrote down car_pool_capacity instead of carpool_capacity

# 1.
# If you use 4.0, all calculations stop being integers and become floats. If
# you change 4.0 to 4, all calculations become integers.
