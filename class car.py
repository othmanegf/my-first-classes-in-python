class Car () :
    def __init__(self, speed, color, nitroSpeed,name, model, enginepower):
        self.speed = speed
        self.color = color
        self.nitroSpeed = nitroSpeed
        self.name = name
        self.model = model
        self.enginepower = enginepower
       
my_car = Car(speed=350, color="black", nitroSpeed=True,name ="MERCEDES", model="G Class(BRABUS)", enginepower="325.86bhp")
print("The max speed is {}".format(my_car.speed))
print("The color is {}".format(my_car.color))
print("The nitrospeed :{}".format(my_car.nitroSpeed))
print("The car's name is: {}".format(my_car.name))
print("The model is: {}".format(my_car.model))
print("Engine power:{}".format(my_car.enginepower))
