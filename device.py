# Створіть клас Device, який містить інформацію про пристрій.
# За допомогою механізму успадкування реалізуйте клас
# Coffee Machine (містить інформацію про кавомашину), клас
# Blender (містить інформацію про блендер), клас MeatGrinder
# (містить інформацію про м’ясорубку).
# Кожен із класів має містити необхідні для роботи методи.

class Device:
    def __init__(self, brand, model, year) -> None:
        self._model = model
        self._year = year
        self._brand = brand
    
    def get_model(self):
        return self._model
    def set_model(self, new_model):
        self._model = new_model

    def get_year(self):
        return self._year
    def set_year(self, new_year):
        self._year = new_year
    
    def get_brand(self):
        return self._brand
    def set_brand(self, new_brand):
        self._brand = new_brand

    def turn_on(self):
        print(f"{self._brand} {self._model} is now turned on.")

    def turn_off(self):
        print(f"{self._brand} {self._model} is now turned off.")

    def __str__(self) -> str:
        return f'Brand:{self._brand}, Model: {self._model}, Year: {self._year}'

class CoffeeMachine(Device):
    def __init__(self, brand, model, year, coffee_type) -> None:
        super().__init__(brand, model, year)
        self._coffeetype = coffee_type
    
    def get_coffee_type(self):
        return self._coffeetype
    def set_coffee_type(self, new_coffee_type):
        self._coffeetype = new_coffee_type
    
    def make_coffee(self):
        print(f"{self._brand} {self._model} making {self._coffeetype}")

    def __str__(self) -> str:
        device_info = super().__str__() 
        return f'{device_info}, Coffee Type: {self._coffeetype}'

class MeatGrinder(Device):
    def __init__(self, brand, model, year, grind_size) -> None:
        super().__init__(brand, model, year)
        self._grindsize = grind_size

    def get_grind_size(self):
        return self._grindsize
    def set_grind_size(self, new_grind_size):
        self._grindsize = new_grind_size
    
    def grind(self):
        print(f"{self._brand} {self._model} grinding with {self._grindsize} grind size")
    
    def __str__(self) -> str:
        device_info = super().__str__() 
        return f'{device_info}, Grind size:{self._grindsize}'

class Blender(Device):
    def __init__(self, brand, model, year, speed_level) -> None:
        super().__init__(brand, model, year)
        self._speedlevel = speed_level
    
    def get_speed_level(self):
        return self._speedlevel
    def set_speed_level(self, new_speed_level):
        self._speedlevel = new_speed_level
    
    def blend(self):
        print(f"{self._brand} {self._model} blending at {self._speedlevel} speed")
    
    def __str__(self) -> str:
        device_info = super().__str__() 
        return f'{device_info}, Speed level:{self._speedlevel}'
    
coffe_machine = CoffeeMachine("a", "b", 1990, 'c')
coffe_machine.turn_on()
coffe_machine.make_coffee()
coffe_machine.turn_off()

blender = Blender('d', 'f', 1234, 5)
blender.turn_on()
blender.blend()
blender.turn_off()

meat_grinder = MeatGrinder('g', 'h', 5635, 8)
meat_grinder.turn_on()
meat_grinder.grind()
meat_grinder.turn_off()