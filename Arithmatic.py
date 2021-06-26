# Store input data in variables
cost_of_ice_bag = 1.25
profit_margin = .2
number_of_bags = 500

# Perform the required calculations
profit_per_bag = cost_of_ice_bag * profit_margin
total_profit = number_of_bags * profit_per_bag
is_icebag_expensive=cost_of_ice_bag>=10

# Display the result
print("The grocery store makes a total profit of $", total_profit)
print("Is the ice bag expensive?",is_icebag_expensive)

bool= not is_icebag_expensive
print(bool)

c=3<5 and 5>3
print(c)

d=4<5 or 1>0
print(d)
