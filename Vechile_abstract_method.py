from abc import abstractmethod

class Vehicle:
    def __init__(self, manufacturer, model, year, type):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.type = type
        self.started = False
        
    def start(self):
        print(f"Starting {self.model}")
        self.started = True
        print(f"{self.model} Started")
    
    def stop(self):
        print(f"Stoping {self.model}")
        self.started = False
        print(f"{self.model} Stopped")
        
    def is_started(self):
        return self.started
        
    @abstractmethod
    def doors(self):
        raise Exception("Doors not defined for this vehicle")
        pass

class Car(Vehicle):
    def __init__(self, manufacturer, model, year, type, no_of_doors):
        self.no_of_doors = no_of_doors
        self.all_doors_closed = True
        super().__init__(manufacturer, model, year, type)
        
    def start(self):
        if not self.all_doors_closed:
            raise Exception("Cannot start, doors are open")
            return
        super().start()
            
    def open_doors(self):
        self.all_doors_closed = False
    
    def close_doors(self):
        self.all_doors_closed = True
    
    def honking(self):
        print("HONK!!!!")
        
    def doors(self):
        return self.no_of_doors
    
    @classmethod
    def what_kind_of_vehicle(cls):
        print("CAR")
        

tesla = Car("tesla", "model 3", 2023, "CAR", 4)
truck = Vehicle("Tata", "rc430", 2011, "TRUCK")

