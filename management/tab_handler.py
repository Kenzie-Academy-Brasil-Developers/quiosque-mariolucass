from menu import products


def calculate_tab(list: list):
    amountTotal = 0

    for object in list:
        for product in products:
            if product["_id"] == object["_id"]:

                amountTotal += product["price"] * object["amount"]

    return {"subtotal": f"${round(amountTotal, 2)}"}
