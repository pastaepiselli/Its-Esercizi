class Room:

    def __init__(self, id: str, piano: str, numero_posti: int, area: int):

        self.id = id 
        self.piano = piano
        self.numero_posti = numero_posti
        self.area = numero_posti * 2

    def get_id(self):

        return self.id
    
    def get_floor(self):

        return self.piano
    
    def get_seats(self):

        return self.numero_posti
    
    def get_area(self):

        return self.area
    

class Building:

    def __init__(self, name: str, address: str, floors: tuple[int, int], rooms: list[Room]):


        self.name = name
        self.address = address
        self.floors = floors
        self.rooms = []

    def get_floors(self):

        return self.floors
    
    def get_rooms(self):

        return self.rooms
    
    def add_room(self, new_room: Room):

        if new_room.get_id not in [stanza.get_id() for stanza in self.rooms]:

            if self.floors[0] <= new_room.get_floor() <= self.floors[1]:
                self.rooms.append(new_room)

            else:

                raise ValueError('')
        else:

            raise ValueError('Aula fuori dall\'intervallo ')

    def area(self):
        sum: int = 0

        for stanze in self.rooms:

            sum += stanze.get_area()


        return sum
        




        