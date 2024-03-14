
class Vechiles:


   def __init__(self,manufactor,model,year,type_vechile):
    self.manufactor = manufactor
    self.model = model
    self.year = year
    self.type_vechile = type_vechile
    self.start = False
    
   def __str__(self):
      return f"{self.manufactor} {self.model} {self.year} {self.type_vechile}"
      
   def starting(self):
      self.start == True
      print(self.manufactor+ " is started")
   def stopping(self):
       self.start = False
       print(self.manufactor+ " is not started")
      
   def is_started(self):
       return self.start
       
      
class Cars(Vechiles):
    
    def __init__(self,manufactor,model,year,type_vechile,no_of_doors):
      self.no_of_doors = no_of_doors
      super().__init__(manufactor,model,year,type_vechile)
      
      
    def honking(self):
       print("it is honking")
    
class Tractors(Vechiles):
      
       def __init__(self,manufactor,model,year,type_vechile,no_of_doors,trailer_locked,fuel_levl):
         self.trailer_locked = trailer_locked
         self.fuel_levl = fuel_levl
         super().__init__(manufactor,model,year,type_vechile)
       def __str__(self):
          return f"{self.manufactor} {self.model}"
         
       def starting(self):
        if self.trailer_locked:
           print("Trailer is unlocked tractor is starting")
        elif self.fuel_levl > 30 and self.fuel_levl < 49:
           print("This is a remainder Tractor fuel is below the half tank")
        elif self.fuel_levl > 49:
           print("Tractor fuel is good")
           super().starting()
     
       def stopping(self):
        if not self.trailer_locked:
           print("Trailer is locked you need to unlock to start the tractor")
        elif self.fuel_levl == 0:
           print("Need to fill the fuel to start the tractor")
           super().stopping()

          
       def is_starting(self):
          return self.trailer_locked
       
          
       @classmethod
       def vech_type(cls):
         print("Tractor")
          
class JohnDeer(Tractors):
    def __init_(Self, self,manufactor,model,year,type_vechile,no_of_doors,trailer_locked,fuel_levl):
     super().__init__(manufactor,model,year,type_vechile)
    def __str__(self):
     return f"{self.year} {self.type_vechile}"
    @classmethod
    def vech_type(cls):
     return cls.__name__    
          
john = Tractors("john_deer","le",2021,"Tractor",6,True,0)

deer = JohnDeer("john_deer","le",2021,"Tractor",6,True,0)

john.starting()
john.stopping()
john.vech_type()

print(deer.vech_type())

