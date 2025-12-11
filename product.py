def product_details(id,name,quantity,price):
    result=(
        f"Product ID:{id}\n"
        f"Name:{name}\n"
        f"Quantity:{quantity}\n"
        f"Price:{price}"
    )
    return result
if __name__=="__main__":
    print(product_details(1001,"Laptop",4,60000))