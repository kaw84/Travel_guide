destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'Sao Paulo, Brazil', 'Cairo, Egypt']

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

attractions = [[] for thing in destinations]


def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index


def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index


def add_attraction(destination, attraction):
    destination_index = get_destination_index(destination)
    attractions_for_destinations = attractions[destination_index].append(attraction)
    return attractions_for_destinations


def find_attractions(destinations, interests):
    destination_index = get_destination_index(destinations)
    attractions_in_city = attractions[destination_index]
    attractions_with_interest = []

    for attraction in attractions_in_city:
        possible_attraction = attraction
        attraction_tags = attraction[1]

        for interest in interests:
            if interest in attraction_tags:
                attractions_with_interest.append(possible_attraction[0])

    return attractions_with_interest


def get_attractions_for_traveler(traveler):
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]
    traveler_attractions = find_attractions(traveler_destination, traveler_interests)

    interests_string = "Hi "
    interests_string = interests_string + traveler[0]
    interests_string = interests_string + ", we think you'll like these places around " + traveler_destination

    for attraction in traveler_attractions:
        interests_string = interests_string + attraction

    return interests_string


add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

la_arts = find_attractions('Los Angeles, USA', ['art'])
print(la_arts)
smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)