class Phone:
    def __init__(self, manufacturer, model, retail_price):
        self.__manufacturer = manufacturer
        self.__model = model
        self.__retail_price = retail_price

    # Accessors
    def get_manufacturer(self):
        return self.__manufacturer

    def get_model(self):
        return self.__model

    def get_retail_price(self):
        return self.__retail_price

    # Mutators
    def set_manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer

    def set_model(self, model):
        self.__model = model

    def set_retail_price(self, retail_price):
        self.__retail_price = retail_price
