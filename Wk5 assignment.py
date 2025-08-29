1.)

1.
   class Smartphone:
       def _init_(self, brand, model, storage):
           self.brand = brand
           self.model = model
           self.storage = storage
   

2. 
       def make_call(self, number):
           print(f"Calling {number} from {self.model}")
   

3. 
   phone1 = Smartphone("Samsung", "Galaxy S21", "128GB")
   phone1.make_call("08123456789")
   

4.
   class Smartwatch(Smartphone):
       def track_steps(self):
           print("Tracking steps...")



2.)

class Car:
    def move(self):
        print("Driving 🚗")

class Plane:
    def move(self):
        print("Flying ✈️")

Polymorphism
for vehicle in (Car(), Plane()):
    vehicle.move()


