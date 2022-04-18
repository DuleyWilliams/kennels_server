ANIMALS = [
    {
        "id": 1,
        "name": "Doodles",
        "species": "Poodle",
        "customerId": 1,
        "location": 2
    },
    {
        "id": 2,
        "name": "Duley",
        "species": "Datsun",
        "customerId": 2,
        "location": 2
    },
    {
        "id": 3,
        "name": "Rob",
        "species": "Rottweiler",
        "customerId": 3,
        "location": 1
    },
    {
        "id": 4,
        "name": "Carl",
        "species": "Corgi",
        "location": 1,
        "customerId": 4
    },
    {
        "id": 5,
        "name": "Snickers",
        "species": "Dog",
        "location": 1,
        "customerId": 4
    },
    {
        "id": 6,
        "name": "Gypsy",
        "species": "Dog",
        "location": 1,
        "customerId": 2
    },
    {
        "id": 7,
        "name": "Blue",
        "species": "Cat",
        "location": 2,
        "customerId": 1
    }
]

# ANIMALS = [
#     {
#         "id": 1,
#         "name": "Snickers",
#         "species": "Dog",
#         "customerId": 4
#     },
#     {
#         "id": 2,
#         "name": "Brixton",
#         "species": "Dog",
#         "customerId": 1
#     },
#     {
#         "id": 3,
#         "name": "Blue",
#         "species": "Cat",
#         "customerId": 5
#     },
#     {
#         "id": 4,
#         "name": "Micky",
#         "species": "Mouse",
#         "customerId": 2
#     },
#     {
#         "id": 5,
#         "name": "Scooby",
#         "species": "Dog",
#         "customerId": 6
#     },
#     {
#         "id": 6,
#         "name": "Jack",
#         "species": "Rabbit",
#         "customerId": 3
#     }
# ]


def get_all_animals():
    return ANIMALS

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

# friend = get_single_animal(3)

# print(friend)


def create_animal(animal):
    # Get the id value of the last animal in the list
    max_id = ANIMALS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    animal["id"] = new_id

    # Add the animal dictionary to the list
    ANIMALS.append(animal)

    # Return the dictionary with `id` property added
    return animal


def delete_animal(id):
    # Initial -1 value for animal index, in case one isn't found
    animal_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            # Found the animal. Store the current index.
            animal_index = index

    # If the animal was found, use pop(int) to remove it from list
    if animal_index >= 0:
        ANIMALS.pop(animal_index)
