from menu import products
from management import product_handler, tab_handler


def main():
    product = {
        "title": "Feijão",
        "price": 5.0,
        "rating": 7,
        "description": "Feijão bonitão camilo",
        "type": "bakery",
    }
    tab = [
        {"_id": 10, "amount": 3},
        {"_id": 20, "amount": 2},
        {"_id": 21, "amount": 5},
    ]
    required_keys = (
        "description",
        "price",
        "rating",
        "title",
        "type",
    )

    # res = product_handler.get_product_by_id(2)
    # res = product_handler.get_products_by_type("fruit")
    # res = product_handler.add_product(products, product)
    # res = tab_handler.calculate_tab(tab)
    # res = product_handler.menu_report()
    # res = product_handler.add_product_extra(products, *required_keys, **product)

    # print(res)


if __name__ == "__main__":
    main()