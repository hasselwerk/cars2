


""" 
Her er coden som jeg har lagt
"""

class Car:
    """
    denne klassen er en super klasse som er for at koder kan gå igjenom. Resten av klassene refere til denne koden  for at alle skal ha en form for uniform verdi.
    Her blir det definert at bilen sine hoved prinsipper og hva som kommer til å bli printet ut som vist nedenfor i print_model og print_space.
    """
    def __init__(self):
        self.type = ""
        self.model = ""
        self.wheels = 4
        self.doors = 3
        self.seets = 5

    def print_model(self):
        print("This car is a {model}: {type}, Wow!".format(model=self.model,type= self.type))

    def print_space(self):
        print("The car has {0} doors and {1} seets".format(self.doors, self.seets))
    def __str__(self):
        return """
This car is a {s.model}: {s.type}, Wow!
The car has {s.doors} doors and {s.seets} seets""".format(s=self)


class BMW(Car):
    """
    Her viser det til at bilen er BMW og er et objekt med i car. Denne referer til super klassen for at den kan sette in sine verdier i samme formel.
    """
    def __init__(self, **arg):
          Car.__init__(self)
          self.model = "BMW"
          self.type = "{} Series".format(arg.get("type"))
          self.doors = arg.get("doors")
          self.fuel = arg.get("fuel")

class Mercedes(Car):
    """
    Her viser det til at bilen er mercedes og er et objekt med i car. Denne referer til super klassen for at den kan sette in sine verdier i samme formel.
    """
    def __init__(self, **arg):
        Car.__init__(self)
        self.model = "Mercedes"
        self.type = "{} Class".format(arg.get("type"))
        self.doors = arg.get("doors")
        self.fuel = arg.get("fuel")


class Fuel:
    """
    Class fuel er drivstoffet som klassene blir referet senere i koden til hvor mye drivstoff bilen har. koden er satt opp slik at en argument senere vil endre på verdien til
    hvor mye drivstoff det er i bilen 
    """
    def __init__(self, **arg):
        self.liters = arg.get("liters")
        self.type = arg.get("type")

    def __str__(self):
        return """It uses {s.liters}L of {s.type}¢.""".format(s=self)


class CarFactory:
    """
    Her skjer det noe med valuen som blir referert i class Carstore.
    """
    def __init__(self, **kwargs):
        self.car = kwargs.get("type")(type=kwargs.get("car_type"),doors=kwargs.get("doors"),fuel=Fuel(liters=kwargs.get("liters"),type=kwargs.get("fuel_type")))

    def get_car(self):
        """Returns en bil"""
        return self.car


class CarStore:
    inventory = []
    """
    Her er lagde biler lagret.
    """
    def __init__(self, **kwargs):
        self._car_factory = CarFactory(type=kwargs.get("type"), car_type=kwargs.get("car_type"),doors=kwargs.get("doors"),liters=kwargs.get("liters"),fuel_type=kwargs.get("fuel_type"))
        self.inventory.append(self._car_factory.get_car())

    def show_car(self, car=None):
        if not car:
            car = self._car_factory.get_car()

        print(car)
        print(car.fuel)

    def show_inventory(self):
        for i in self.inventory:
            self.show_car(i)

    def __str__(self):
        return "".join([str(i) for i in self.inventory])

"""

Her er argumenten som blir presentert og skapåer en vaule
"""
store = CarStore(type=Mercedes, car_type= "E", doors=2, liters = 2,fuel_type = "Disel")
store2 = CarStore(type=Mercedes, car_type= "C", doors=4, liters = 2,fuel_type = "Disel")
store3 = CarStore(type=BMW, car_type="1", doors= 3, liters= 2.5, fuel_type = "Gasoline")
store.show_inventory()



print("\n","-"*100)


class Lada(Car):
    """
    Her er en til bil
    """
    def __init__(self, **arg):
        Car.__init__(self)
        self.model = "Lada"
        self.type = "{}".format(arg.get("type"))
        self.doors = arg.get("doors")
        self.fuel = arg.get("fuel")

store = CarStore(type=Lada, car_type="VAZ-2107",doors=2,liters=1.2,fuel_type="Octane Gasoline")

store.show_inventory()


