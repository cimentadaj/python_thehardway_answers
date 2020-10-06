# create a mapping of state to abbreviation
states = {
    'Catalonia': 'CAT',
    'Madrid': 'MAD',
    'Andalucia': 'AND',
    'Asturias': 'AST',
    'Pais Vasco': 'PV'
}

# create a basic set of states and some cities in them
cities = {
    'CAT': 'Barcelona',
    'AND': 'Sevilla',
    'AST': 'Oviedo'
}

# add some more cities
cities['MAD'] = 'Madrid'
cities['PV'] = 'Bilbao'

# print out some cities
print("-" * 10)
print("Catalonia state has: ", cities['CAT'])
print("Andalucia state has: ", cities['AND'])

# print some states
print("-" * 10)
print("Pais Vasco's abbreviation is: ", states['Pais Vasco'])
print("Asturias abbreviation is: ", states['Asturias'])

# do it by using the state then cities dict
print("-" * 10)
print("Catalonia has: ", cities[states['Catalonia']])
print("Andalucia has: ", cities[states['Andalucia']])

# print every state abbreviation
print("-" * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print("-" * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print("-" * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")


print("-" * 10)
# safely get abbreviation by state that might not be there
state = states.get("Extremadura")

if not state:
    print("Sorry, no Extremadura.")

# get a city with a default value
city = cities.get("EXT", 'Does Not Exist')
print(f"The city for the state 'EXT' is: {city}")
