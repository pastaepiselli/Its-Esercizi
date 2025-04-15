from datetime import datetime
class Dates:

    def __init__(self):

        self.database: list[str] = []

    def date(self, new_date: str):

        if len(new_date) != 10:

            raise ValueError('Inserire una data valida')
        
        if new_date[2] != '.' or new_date[5] != '.':

            raise ValueError('Inserire . come separatore')
        
        try:
            # y = anni rappresentati con 00, Y = anni rappresentati con 0000
            
            datetime.strptime(new_date, '%d.%m.%Y')     
            return True
        
        
        except ValueError:

            raise ValueError('La data inserita non e del formato valido')


    def add_date(self, new_date: str):

        if self.date(new_date):
            if new_date in self.database:
                print('data gia inserita')
            else:
                print('data aggiunta')
                self.database.append(new_date)

    def delete_date(self, date: str):

        if date in self.database:

            self.database.remove(date)
            print('data rimossa con successo!!')
        
        else:

            print('la data non e presente nel database')

    def modify_date(self, mod_date: str):


        if mod_date in self.database:
            print('Inserire nuova data')
            p = str(input(''))
            if self.date(p):
                self.database[self.database.index(mod_date)] = p
                print('Data cambiata con successo')
    def query_date(self, searchdate: str):


        if self.date(searchdate):

            if searchdate in self.database:

                print('La data e nel database')

            else:

                print('La data non e nel data base, desidera aggiungerla?')
                n = str(input('S / N: '))

                if n.lower() == 's':

                    self.add_date(searchdate)

                    

                       
                    
                    





    




mydate:Dates = Dates()


mydate.add_date('18.05.2004')

mydate.query_date("19.05.2004")
        
