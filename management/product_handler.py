from menu import products
from collections import Counter
from numpy import average


def get_product_by_id(id: int) -> dict:
    if type(id) is not int:
        raise TypeError("product id must be an int")

    for product in products:
        if product["_id"] == id:
            return product
    return {}


def get_products_by_type(typeParam: str) -> list:
    if type(typeParam) is not str:
        raise TypeError("product type must be a str")

    products_with_same_type = []

    for product in products:
        if product["type"] == typeParam:

            products_with_same_type.append(product)

    if len(products_with_same_type):
        return products_with_same_type
    return []


def add_product(menu: list, **product: dict) -> dict:
    product["_id"] = len(menu) + 1
    menu.append(product)
    return product


def menu_report() -> str:
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


def add_product_extra(menu: list, *required_keys: dict, **product: dict) -> dict:
    keys_product = [*product]
    keys_required = [*required_keys]

    for key in keys_required:
        if key not in keys_product:
            raise KeyError(f"field {key} is required")

    for key in keys_product:
        if key not in keys_required:
            product.pop(key)

    product["_id"] = len(menu) + 1
    menu.append(product)
    return product
