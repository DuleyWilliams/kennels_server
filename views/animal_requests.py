ANIMALS = [
    {
        "id": 1,
        "name": "Doodles",
        "breed": "Poodle",
        "customerId": 1,
        "locationId": 2
    },
    {
        "id": 2,
        "name": "Duley",
        "breed": "Datsun",
        "customerId": 2,
        "locationId": 2
    },
    {
        "id": 3,
        "name": "Rob",
        "breed": "Rottweiler",
        "customerId": 3,
        "locationId": 1
    },
    {
        "id": 4,
        "name": "Carl",
        "breed": "Corgi",
        "customerId": 4,
        "locationId": 1
    },
    {
        "id": 5,
        "name": "Snickers",
        "species": "Dog",
        "locationId": 1,
        "customerId": 4
    },
    {
        "id": 6,
        "name": "Gypsy",
        "species": "Dog",
        "locationId": 1,
        "customerId": 2
    },
    {
        "id": 3,
        "name": "Blue",
        "species": "Cat",
        "locationId": 2,
        "customerId": 1
    }
]


# def get_all_animals():
#     return ANIMALS

# Function with a single parameter
def get_single_animal(id):
    # Variable to hold the found animal, if it exists
    requested_animal = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for animal in ANIMALS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if animal["id"] == id:
            requested_animal = animal

    return requested_animal
