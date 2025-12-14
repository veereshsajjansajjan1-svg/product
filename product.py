def product_info(product_id, name, quantity, price):
    return (
        f"Product Details:\n"
        f"ID: {product_id}\n"
        f"Name: {name}\n"
        f"Quantity: {quantity}\n"
        f"Price: {price}"
    )


if __name__ == "__main__":
    print(product_info(101, "Laptop", 5, 55000))
