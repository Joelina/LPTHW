cars = 100 #defines that there are 100 cars
space_in_a_car = 4.0 #defines that there are 4 spaces in a car
drivers = 30 #defines that there are 30 drivers
passengers = 90 # defines that there are 90 passenger
cars_not_driven = cars - drivers #when subtract the drivers from the cars you get how many cars aren't driven
cars_driven = drivers #depending on how many drivers you have, that many cars can be driven
carpool_capacity = cars_driven * space_in_a_car #calculates the carpool capacity
average_passengers_per_car = passengers / cars_driven #calculates how many passengers per car on average


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
