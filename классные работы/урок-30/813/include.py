#================================┌───┐========================================#
#================================│┌─┐│========================================#
#================================││█││========================================#
#================================│└─┘│========================================#
#================================│┌─┐│========================================#
#================================└┘█└┘========================================#
class Shop():                                   #┌───┐
                                                #│┌─┐│
                                                #││█└┘
                                                #││█┌┐
                                                #│└─┘│
                                                #└───┘                             
    def __init__(self,shop_name,store_type,number_of_units):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = number_of_units
        number_of_units = 0
    def describe_shop(self):
        print(f'\n\nShop name: {self.shop_name}\nStore type: {self.store_type}\nNumbers of units: {self.number_of_units}')
    def open_shop(self):
        print(f'Online shop \'{self.shop_name}\' is open.')
    #================================┌───┐================================#
    #================================└┐┌┐│================================#
    #================================█││││================================#
    #================================█││││================================#
    #================================┌┘└┘│================================#
    #================================└───┘================================#
    def set_number_of_units(self,new_numbers_of_units):
        self.number_of_units = new_numbers_of_units
        print(f'New numbers of units: {self.number_of_units}')
    def increment_number_of_units(self,value):
        self.number_of_units+=value
        print(f'Increment numbers of units: {self.number_of_units}')