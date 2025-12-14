from product import product_info

def test_product_info():
    expected = (
        "Product Details:\n"
        "ID: 101\n"
        "Name: Laptop\n"
        "Quantity: 5\n"
        "Price: 55000"
    )

    result = product_info(101, "Laptop", 5, 55000)

    assert result == expected
