class Car:
    """
    Docstring describing the class
    It models a car with tyres and engines
    """

    def __init__(self, engine, tires):
        """
        Docstring describing the method
        It runs when a child object is instanced
        >>> civic = Car('4-cyl', ['fd', 'fp', 'rd', 'rp'])
        """
        self.engine = engine
        self.tires = tires

    def description (self):
        """
        It will return a short desciption of the car
        >>> from Tire import Tire
        >>> tire = Tire('P', 205, 65, 15)
        >>> tires = [tire, tire, tire, tire]
        >>> civic = Car(tires=tires, engine='4-cyl')
        >>> civic.description()
        A car with 4-cyl engine and 4 tires type P 205/65 R 15
        """
        tirecount = int(len(self.tires))
        print (f'A car with {self.engine} engine and {tirecount} tires type {self.tires[0]}' )

    def wheel_circumference(self):
        if len(self.tires) > 0:
            return self.tires[0].circumference()
        else:
            return 0
