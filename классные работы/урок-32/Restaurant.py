class Restaurant:
    def __init__(self,restaurant_name,cuisine_type,number_served=0):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=number_served
    def describe_restaurant(self):
        print(f"Restaurant '{self.restaurant_name.title()}' have {self.cuisine_type} cuisine")
    def open_restaurant(self):
        print("Restaurant open!")
    def set_number_served(self,new_number_served):
        self.number_served=new_number_served
        return self.number_served
    def increment_number_served(self,time):
        print(self.number_served+(10*time))
