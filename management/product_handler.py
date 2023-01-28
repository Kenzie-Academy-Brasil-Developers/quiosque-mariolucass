import numpy
from menu import products
from collections import Counter


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
    avg_price = []
    common_types = []

    for product in products:
        avg_price.append(product["price"])
        common_types.append(product["type"])

    common_type = Counter(common_types).most_common(1)[0][0]
    avg_price = numpy.mean(avg_price)
    avg_price = round(avg_price, 2)

    return f"Products Count: {menu_length} - Average Price: ${avg_price} - Most Common Type: {common_type}"
