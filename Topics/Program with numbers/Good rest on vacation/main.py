days = int(input())
food_cost = int(input())
flight_cost = int(input())
night_cost = int(input())

cost = (food_cost * days) + (flight_cost * 2) + (night_cost * (days - 1))

print(cost)
