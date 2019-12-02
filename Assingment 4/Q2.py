Q2:Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city
  and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary
  should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.




cities = {
    'santiago': {
        'country': 'chile',
        'population': 6158080,
        'nearby mountains': 'andes',
        },
    'talkeetna': {
        'country': 'alaska',
        'population': 876,
        'nearby mountains': 'alaska range',
        },
    'kathmandu': {
        'country': 'nepal',
        'population': 1003285,
        'nearby mountains': 'himilaya',
        }
    }

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    mountains = city_info['nearby mountains'].title()

    print("\n" + city.title() + " is in " + country + ".")
    print("  It has a population of about " + str(population) + ".")
    print("  The " + mountains + " mountains are nearby.")




Output:

Santiago is in Chile.
  It has a population of about 6158080.
  The Andes mountains are nearby.

Talkeetna is in Alaska.
  It has a population of about 876.
  The Alaska Range mountains are nearby.

Kathmandu is in Nepal.
  It has a population of about 1003285.
  The Himilaya mountains are nearby.