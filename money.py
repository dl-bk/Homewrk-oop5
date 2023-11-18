# Запрограмуйте клас Money (об’єкт класу оперує однією
# валютою) для роботи з грошима.
# У класі мають бути передбачені: поле для зберігання цілої
# частини грошей (долари, євро, гривні тощо) і поле для зберігання копійок (центи, євроценти, копійки тощо).

# Реалізуйте методи виведення суми на екран, задання
# значень частин.
# Створіть клас Product для роботи з продуктом або товаром беручи за основу клас Money. Реалізуйте метод для
# зменшення ціни на задане число.
# Для кожного з класів реалізуйте необхідні методи та поля.

class Money:
    def __init__(self, dollars, cents) -> None:
        self._dollars = dollars
        self._cents = cents
    

    def set_money(self, dollars, cents):
        self._dollars = dollars
        self._cents = cents
    
    def __str__(self) -> str:
        return f'Dollars: {self._dollars}, Cents:{self._cents:02d}'
    
class Product(Money):
    def __init__(self, name, dollars, cents) -> None:
        super().__init__(dollars, cents)
        self._name = name

    def decrease_price(self, decr_dollars, decr_cents):
        total_cents = ((self._dollars * 100) + self._cents) - ((decr_dollars * 100) + decr_cents)
        self._dollars, self._cents = divmod(total_cents, 100)

    def __str__(self) -> str:
        money_info = super().__str__()
        return f"Name:{self._name}, {money_info}"


product = Product('a', 10, 23)
product.decrease_price(4, 20)
print(product) 
