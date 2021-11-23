class Venicle():
    def vehicle(self, y, place, passengers, speed):
        self.y = y
        self.place = place
        self.passengers = passengers
        self.speed = speed
        print(self.y, self.place, self.passengers, self.speed)

class AirCraft(Venicle):
    def plane(self, y, passengers):
        self.y = y
        self.passengers = passengers
        print(self.y, self.passengers)

class Car(Venicle):
    def car(self, speed, passengers):
        self.speed = speed
        self.passengers = passengers
        print(self.speed, self.passengers)

class Ship(Venicle):
    def ship(self, place, passengers):
        self.place = place
        self.passengers = passengers
        print(self.place, self.passengers)

a = AirCraft()
a.plane("40 метрів висоти", "100 пасажирів")
b = Car()
b.car("80 км/год", "2 пасажира")
c = Ship()
c.ship("Порт приписки: Лондон", "200 пасажирів")