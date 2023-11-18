# Створіть клас Ship, який містить інформацію про кораблі.
# За допомогою механізму успадкування реалізуйте клас
# Frigate (містить інформацію про фрегат), клас Destroyer(містить
# інформацію про есмінця), клас Cruiser (містить інформацію
# про крейсер).
# Кожен із класів має містити необхідні для роботи методи.

class Ship:
    def __init__(self, ship_name, year, capacity, max_speed) -> None:
        self._name = ship_name
        self._year = year
        self._capacity = capacity
        self._maxspeed = max_speed
    
    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name
    
    def get_year(self):
        return self._year
    def set_year(self, year):
        self._year = year
    
    def get_capacity(self):
        return self._capacity
    def set_capacity(self, capacity):
        self._capacity = capacity
    
    def get_max_speed(self):
        return self._maxspeed
    def set_max_speed(self, max_speed):
        self._maxspeed = max_speed
    
    def sail(self):
        print(f"{self._name} is sailing.")
    
    def __str__(self) -> str:
        return f"Name: {self._name}, Year: {self._year}, Capacity: {self._capacity}, Max Speed: {self._maxspeed}"

class Fregate(Ship):
    def __init__(self, ship_name, year, capacity, max_speed, missiles) -> None:
        super().__init__(ship_name, year, capacity, max_speed)
        self._missiles = missiles
    
    def get_missiles(self):
        return self._missiles
    def set_missiles(self, missiles):
        self._missiles = missiles
    
    def launch_missile(self):
        print(f"{self._name} launched {self._missiles} missiles.")

    def __str__(self) -> str:
        ship_info = super().__str__() 
        return f"{ship_info}, Missiles: {self._missiles}"

class Destroyer(Ship):
    def __init__(self, ship_name, year, capacity, max_speed, cannons) -> None:
        super().__init__(ship_name, year, capacity, max_speed)
        self._cannons = cannons
    
    def get_cannons(self):
        return self._cannons
    def set_cannons(self, cannons):
        self._cannons = cannons
    
    def fire_cannons(self):
        print(f"{self._name} fired {self._cannons} cannons.")

    def __str__(self) -> str:
        ship_info = super().__str__() 
        return f"{ship_info}, Cannons: {self._cannons}"

class Cruiser(Ship):
    def __init__(self, ship_name, year, capacity, max_speed, torpedoes) -> None:
        super().__init__(ship_name, year, capacity, max_speed)
        self._torpedoes = torpedoes
    
    def get_cannons(self):
        return self._torpedoes
    def set_cannons(self, torpedoes):
        self._torpedoes = torpedoes
    
    def launch_torpedo(self):
        print(f"{self._name} launched {self._torpedoes} torpedoes.")

    def __str__(self) -> str:
        ship_info = super().__str__() 
        return f"{ship_info}, Torpedoes: {self._torpedoes}"


fregate = Fregate('a', 1998, 3000, 60, 30)
destroyer = Destroyer('b', 2006, 10000, 70, 25)
cruiser = Cruiser('c', 1999, 2000, 90, 100)

fregate.sail()
fregate.launch_missile()
print(fregate)

destroyer.sail()
destroyer.fire_cannons()
print(destroyer)

cruiser.sail()
cruiser.launch_torpedo()
print(cruiser)