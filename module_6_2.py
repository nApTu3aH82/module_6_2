class Vehicle:
    __COLOR_VARIANTS = ['blue', 'black', 'white', 'green', 'red']

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def set_color(self, new_color):
        self.new_color = new_color
        color_bol = False
        for color in Vehicle.__COLOR_VARIANTS:
            if new_color.lower() == color.lower():
                color_bol = True
        if color_bol == False:
            print(f'Нельзя сменить цвет на {self.new_color}')
        else:
            self.__color = new_color

    def get_model(self):
        print(f"Модель: {self.__model}")

    def gethorsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}')

    def getcolor(self):
        print(f"Цвет: {self.__color}")

    def print_info(self):
        self.get_model()
        self.gethorsepower()
        self.getcolor()
        print(f'Владелец: {self.owner}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan("Fedos", "Toyota Mark 2", "blue", 500)
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()
