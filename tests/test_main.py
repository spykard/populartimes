''' Query Google's PopularTimes in circles, given latitute and longtitude positions and retrieve data for places/stores '''
import configparser
import populartimes

# Config Parsing
config = configparser.ConfigParser()
config.read('config/config.ini')

mode = eval(config['Settings']['mode'])

if (mode == 1):
    # Get Data by ID
    api_key = config['Settings']['api_key']
    place_id = config['Settings']['place_id']
    data = populartimes.get_id(api_key=api_key, place_id=place_id)
    data = [data]

# Warning can be incredibly costly
elif (mode == 2):
    # Get Data by Circular Location
    api_key = config['Settings']['api_key']
    types = config['Settings']['types'].split(",")
    p1 = eval(config['Settings']['p1'])
    p2 = eval(config['Settings']['p2'])
    radius = eval(config['Settings']['radius'])
    all_places = eval(config['Settings']['all_places'])

    data = populartimes.get(api_key=api_key, types=types, p1=p1, p2=p2, n_threads=20, radius=radius, all_places=all_places)

    print(len(data))
    for place in data:
        print(place['name'])
        print(place['address'])
        print(place['types'])
        print(str(place['rating']) + " (" + str(place['rating_n']) + ")")
        if "current_popularity" in place:
            print(place['current_popularity'])
        else:
            print("N/A")
        print(place['populartimes'])
        if "time_spent" in place:
            print(place['time_spent'])
        else:
            print("N/A")
        print()

elif (mode == 3):
    # Get Data by Crawling Google Maps itself, using two keywords which are combined
    # returns: (rating, rating_n, popular_times, current_popularity, time_spent)
    search_name = config['Settings']['search_name']
    search_address = config['Settings']['search_address']

    place = populartimes.get_popular_times_by_crawl(name=search_name, address=search_address)

    print(search_name + " " + search_address)
    print(str(place['rating']) + " (" + str(place['rating_n']) + ")")
    if "current_popularity" in place:
        print(place['current_popularity'])
    else:
        print("N/A")
    print(place['populartimes'])
    if "time_spent" in place:
        print(place['time_spent'])
    else:
        print("N/A")
    print()