from customer import Customer

c1 = Customer("bronze")
c2 = Customer("gold")
c3 = Customer("platinum")

def get_discount(customer):
    discounts = {
        "bronze": .1,
        "gold": .2,
        "platinum": .35
    }

    discount = discounts.get(customer.loyalty, None)

    if not discount:
        raise ValueError("Could not determine the customer's discount")

    return discount

for customer in(c1,c2,c3):
    print(f"{get_discount(customer):.0%}")