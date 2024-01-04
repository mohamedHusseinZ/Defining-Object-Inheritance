class Car:
    def __init__(self, color, name, model):
        self.color = color
        self.name = name
        self.model = model
    def sort(self):
        return(f"name: {self.name}, color: {self.color}, model: { self.model}") 


car1 = Car("red", "subaru", "toyota")
print(car1.sort())



