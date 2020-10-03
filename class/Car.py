class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name (self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model 
        return long_name.title()

    def read_odometer(self):
            print (self.odometer)
    
    def update_odometer(self, new_odometer):
        if self.odometer <= new_odometer:
            self.odometer = new_odometer
        else: 
            print ("you can't roll back an odometer")

    def increase_odometer(self, increase_mile):
        self.odometer+= increase_mile


class Battery():
    def __init__(self, battery_size = 60):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        range = self.battery_size * 3.5
        message = "this car can go approximately" + str (range)
        message+= " miles on a full charge"
        print (message)

    def ElectricCar (Car):
        def __init__(self, make, model, year):
            super().__init__(make, model, year)
            self.battery = Battery()



