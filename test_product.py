from product import product_details
def test_product_details():
    result=product_details(1001,"Laptop",4,60000)
    expected_output=(
        "Product ID:1001\n"
        "Name:Laptop\n"
        "Quantity:4\n"
        "Price:60000"
    )
    assert result==expected_output