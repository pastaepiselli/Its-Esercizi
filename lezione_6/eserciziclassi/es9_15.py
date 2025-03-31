import random
class LotteryMachine:

    def __init__(self):
        #possibilita
        self.lottery = [3, 45, 6, 2, 6, 1, 86, 23, 4, 5, 't', 'r', 'n', 'q' , 'x']

    def draw_ticket(self):
        #creo un biglietto, che poi sara cambiato finche nn sara come il mio quindi e sbagliato chiamarlo vincente
        self.winning_ticket = random.sample(self.lottery, 4)

    def display_message(self):

        print('Any ticket matching the winning 4 items wins a prize')

    def simulate_until_win(self, myticket):
        #definisco il primo biglietto fuori dal ciclo senno devo richiamare la funzione anche fuori dalla classe perche nn ho nessun biglitto generato
        self.draw_ticket()
        self.attempts: int = 0
        #autoesplicativo
        while self.winning_ticket != myticket:
            
            #nel caso in cui il biglietto nn sia valido
            if len(myticket) > 4:

                print('ticket not valid')
                break
            
            #continuo a cambiare il biglietto finche nn diventa uguale al mio
            self.draw_ticket()

            #tengo conto delle iterazioni
            self.attempts += 1

        return self.attempts, self.winning_ticket
            


lotto = LotteryMachine()
myticket = [2, 'r', 86, 'q']


lotto.simulate_until_win(myticket)

print(f'"Il mio ticket e {myticket}\nIl biglietto vincente e {lotto.winning_ticket}\nCi sono voluti {lotto.attempts} tentativi')


