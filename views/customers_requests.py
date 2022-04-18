CUSTOMERS = [
    {
        "id": 1,
        "name": "Hannah Hall",
        "address": "7002 Chestnut Ct",
        "phoneNumber": "(615) 555-1211",
        "email": "hannah@test.com"
    },
    {
        "id": 2,
        "name": "Duley Williams",
        "address": "500 Rover Bend Dr",
        "phoneNumber": "(615) 832-5555",
        "email": "duley@test.com"
    },
    {
        "id": 3,
        "name": "Robert Richardson",
        "address": "1212 Technique Trail",
        "phoneNumber": "(615) 333-2400",
        "email": "robert@test.com"
    },
    {
        "id": 4,
        "name": "Carl Thompson",
        "address": "978 Broadway",
        "phoneNumber": "(615) 444-1211",
        "email": "carl@test.com"
    },
    {
        "email": "asauce@test.com",
        "name": "Awesome Sauce",
        "id": 5
    },
    {
        "email": "dtest@me.com",
        "name": "Dtest Me",
        "id": 6
    }
]


# CUSTOMERS = [
#     {
#         "id": 1,
#         "name": "Grace",
#         "age": 24
#     },
#     {
#         "id": 2,
#         "name": "Josh",
#         "age": 18
#     },
#     {
#         "id": 3,
#         "name": "Jeff",
#         "age": 37
#     },
#     {
#         "id": 4,
#         "name": "Jamal",
#         "age": 41
#     },
#     {
#         "id": 5,
#         "name": "Megan",
#         "age": 28
#     },
#     {
#         "id": 6,
#         "name": "Caroline",
#         "age": 64
#     }
# ]


def get_all_customers():
    return CUSTOMERS

# Function with a single parameter


def get_single_customer(id):
    # Variable to hold the found customer, if it exists
    requested_customer = None

    # Iterate the CUSTOMERS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer


def create_customer(customer):
    # Get the id value of the last animal in the list
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    customer["id"] = new_id

    # Add the customer dictionary to the list
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer


def delete_customer(id):
    # Initial -1 value for customer index, in case one isn't found
    customer_index = -1

    # Iterate the CUSTOMERS list, but use enumerate() so that you
    # can access the index value of each item
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Store the current index.
            customer_index = index

    # If the customer was found, use pop(int) to remove it from list
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)
