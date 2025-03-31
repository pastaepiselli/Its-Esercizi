class Restaurant:
    def __init__(self, restaurant_name, cusine_type, number_served = 0):
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(self.restaurant_name, self.cusine_type)

    def open_restaurant(self):
        print('The restaurant is open')

    def set_number_served(self, new_clients):

        self.number_served = new_clients

    def increment_number_served(self, served):

        self.number_served += served

    



# granu = Restaurant('Granu', 'italian')   

# print(granu.number_served)

# granu.number_served = 3
# print(granu.number_served)

# granu.set_number_served(7)
# print(granu.number_served)

# granu.increment_number_served(7)
# print(granu.number_served)


