import random
class LotteryMachine:

    def __init__(self):
        
        self.lottery = [3, 45, 6, 2, 6, 1, 86, 23, 4, 5, 't', 'r', 'n', 'q' , 'x']

    def draw_winning(self):

        self.winning_ticket = random.sample(self.lottery, 4)

    def display_message(self):

        print('Any ticket matching the winning 4 items wins a prize')