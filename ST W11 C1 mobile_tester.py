from mobile import Phone

if __name__ == "__main__":
    phone1 = Phone("Manufacturer1", "Model1", "$1000")

    phone1.set_manufacturer(input("Enter the manufacturer: "))
    phone1.set_model(input("Enter the model number: "))
    phone1.set_retail_price(input("Enter the retail price: "))

    print("Phone Manufacturer: ", phone1.get_manufacturer())
    print("Phone Model: ", phone1.get_model())
    print("Retail Price: $", phone1.get_retail_price())
