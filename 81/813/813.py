from include import Shop
all_store = Shop('all_store-Rozetka','all_store-Ishop',0)
all_store.describe_shop()
all_store.open_shop()
all_store.set_number_of_units(20000)
all_store.increment_number_of_units(45)
store = Shop('Rozetka','Ishop',0)
store.describe_shop()
store.open_shop()
store.set_number_of_units(20000)
store.increment_number_of_units(45)
store2 = Shop('Rozetka2','Ishop2',0)
store2.describe_shop()
class Discount(Shop):
    def __init__(self, shop_name, store_type, number_of_units,discount_products):
        super().__init__(shop_name, store_type, number_of_units)
        self.discount_products = discount_products
    def get_discount_products(self):
        print(f'Discount products: {self.discount_products}')
store_discount = Discount('Discount-Rozetka','Ishop',0, 'PC,MAC, IPhone')
store_discount.describe_shop()
store_discount.get_discount_products()
















