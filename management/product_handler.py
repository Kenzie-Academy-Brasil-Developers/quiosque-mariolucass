from menu import products
from collections import Counter
from numpy import average


def get_product_by_id(id: int):

    if type(id) is not int:
        raise TypeError("product id must be an int")

    for product in products:
        if product["_id"] == id:
            return product

    return {}


def get_products_by_type(typeParam: str):

    if type(typeParam) is not str:
        raise TypeError("product type must be a str")

    products_type = []

    for product in products:
        if product["type"] == typeParam:
            products_type.append(product)

    if len(products_type):

        return products_type

    return []


def add_product(menu, **product):
    if len(menu) == 0:
        product["_id"] = 1
    else:
        product["_id"] = len(menu) + 1

    menu.append(product)

    return product
    ...


def menu_report():
    menu_length = len(products)
    prices = []
    types = []

    for product in products:
        prices.append(product["price"])
        types.append(product["type"])

    counter_of_types = Counter(types)
    common_type = counter_of_types.most_common(1)[0][0]

    avg_price = average(prices)

    avg_price = round(avg_price, 2)

    return f"Products Count: {menu_length} - Average Price: ${avg_price} - Most Common Type: {common_type}"


def add_product_extra(menu, *required_keys, **product):
    for key in required_keys:
        print(key)
        print(product[f"{key}"], key)

        # if product["key"] not in required_keys:
        #     raise KeyError(f"field {key} is required")
