import math
def cost_of_trip(city,duration):
    Cost=city['flight_cost']*2+city['hotel_rate']*duration+math.ceil(city['car_rental']*(duration/7))
    return Cost

Paris={
    'flight_cost':200,
    'hotel_rate': 20,
    'car_rental': 200
}

London={
    'flight_cost':250,
    'hotel_rate':30,
    'car_rental':120
}

Dubai={
    'flight_cost': 370,
    'hotel_rate':15,
    'car_rental':80
}

Mumbai={
    'flight_cost':450,
    'hotel_rate':10,
    'car_rental':70
}
list=[]
c=[4,10,14]
for i in c:
    Trips=[{'city':'Mumbai', 'cost': cost_of_trip(Mumbai,i)},{'city':'London','cost': cost_of_trip(London,i)},{'city':'Dubai','cost': cost_of_trip(Dubai,i)},{'city':'Paris','cost': cost_of_trip(Paris,i)}]
    min=10000000
    b=''
    for costs in Trips:
        if costs['cost']<min:
            min=costs['cost']
            b=costs['city']
    list.append(b)

print(list)