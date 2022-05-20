from faker import Faker
from faker.providers import BaseProvider
import random
import csv
from tqdm import tqdm

MAX_ROWS = 10**3

fake = Faker()

#############
# Customers
#############

customer_id = 0

def get_customer_id(customer_id):
    return customer_id

def get_name():
    return fake.name()

def get_email():
    return fake.ascii_safe_email()

def get_phone():
    return fake.msisdn()

#############
# Payments
#############

payment_id = 0

def get_payment_id(payment_id):
    return payment_id

def get_amount():
    return round(random.uniform(1.0, 100.0), 1)

def get_datetime():
    return fake.iso8601()

def get_int_range():
    return random.choice([1, 2, 3, 4, 5])

############
# Orders
############

order_id = 0

def get_order_id(order_id):
    return order_id

#############
# Address
#############

def get_address():
    return fake.address()

#################
# Order Details
#################

def get_quantity():
    return random.randrange(1, 10)

########
# Menu
########

menu_id = 0

def get_menu_id(menu_id):
    return menu_id

def get_item_name():
    return fake.color_name()

def get_description():
    return ' '.join(fake.words())

#########################
# Generate mock record
#########################

def generate_customer(customer_id):
    return [get_customer_id(customer_id), get_name(), get_email(), get_phone()]

def generate_payment(payment_id, order_id, customer_id):
    return [get_payment_id(payment_id), get_amount(), get_datetime(), get_int_range(), get_order_id(order_id), get_customer_id(customer_id)]

def generate_order(order_id):
    return [get_order_id(order_id), get_datetime(), get_int_range()]

def generate_address(customer_id, order_id):
    return [get_customer_id(customer_id), get_order_id(order_id), get_address()]

def generate_order_details(order_id, menu_id):
    return [get_order_id(order_id), get_menu_id(menu_id), get_quantity(), get_amount()]

def generate_menu(menu_id):
    return [get_menu_id(menu_id), get_item_name(), get_amount(), get_description()]

####################
# Write to csvs
####################

with open('seeds/customers_seed.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'full_name', 'email', 'phone'])
    for n in tqdm(range(1, MAX_ROWS), desc="Customers Seed"):
        customer_id += 1
        writer.writerow(generate_customer(customer_id))

with open('seeds/orders_seed.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'datetime', 'status'])
    for n in tqdm(range(1, MAX_ROWS), desc="Orders Seed"):
        order_id += 1
        writer.writerow(generate_order(order_id))

with open('seeds/payments_seed.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'amount', 'datetime', 'method', 'order_id', 'customer_id'])
    customer_id = 0
    order_id = 0
    for n in tqdm(range(1, MAX_ROWS), desc="Payments Seed"):
        payment_id += 1
        customer_id += 1
        order_id += 1
        writer.writerow(generate_payment(payment_id, order_id, customer_id))

with open('seeds/address_seed.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['customer_id', 'order_id', 'address'])
    customer_id = 0
    order_id = 0
    for n in tqdm(range(1, MAX_ROWS), desc="Address Seed"):
        customer_id += 1
        order_id += 1
        writer.writerow(generate_address(customer_id, order_id))

with open('seeds/menu_seed.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'price', 'description'])
    for n in tqdm(range(1, MAX_ROWS), desc="Menu Seed"):
        menu_id += 1
        writer.writerow(generate_menu(menu_id))

with open('seeds/order_details_seed.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['order_id', 'menu_id', 'quantity', 'amount'])
    menu_id = 0
    order_id = 0
    for n in tqdm(range(1, MAX_ROWS), desc="Order Details Seed"):
        menu_id += 1
        order_id += 1
        writer.writerow(generate_order_details(order_id, menu_id))
