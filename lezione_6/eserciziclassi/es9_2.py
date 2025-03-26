class Restaurant:
    def __init__(self, restaurant_name, cusine_type):
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type

    def describe_restaurant(self):
        print(self.restaurant_name, self.cusine_type)

    def open_restaurant(self):
        print('The restaurant is open')

    
restaurant = Restaurant('granu', 'italian')
print(restaurant.restaurant_name)
print(restaurant.cusine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()


dagiacomo = Restaurant('pizza da giacomo', 'pizza')
mario = Restaurant('pasta da mario', 'pasta italiana')
hanami = Restaurant('Hanami', 'sushi')

dagiacomo.describe_restaurant()
mario.describe_restaurant()
hanami.describe_restaurant()