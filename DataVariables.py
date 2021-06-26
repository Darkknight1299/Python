color1, color2, color3 = "red", "green", "blue"
color4 = color5 = color6 = "magenta"
a_variable = 23
is_today_Saturday = False
my_favorite_car = "Delorean"
the_3_musketeers = ["Athos", "Porthos", "Aramis"]
type(a_variable)
# Input variables
cost_of_ice_bag = 1.25
profit_margin = .2
number_of_bags = 500

# Template for output message
output_template = """If a grocery store sells ice bags at $ {} per bag, with a profit margin of {} %, 
then the total profit it makes by selling {} ice bags is $ {}."""

print(output_template)
# Inserting values into the string
total_profit = cost_of_ice_bag * profit_margin * number_of_bags
output_message = output_template.format(cost_of_ice_bag, profit_margin*100, number_of_bags, total_profit)

print(output_message)

fruits = ('apple', 'cherry', 'dates')#this is a tuple, cant change its values

#this is dictionary
person1 = {
    'name': 'John Doe',
    'sex': 'Male',
    'age': 32,
    'married': True
}

person2 = dict(name='Jane Judy', sex='Female', age=28, married=False)

person1['address'] = '1, Penny Lane'