
class ValueError(Exception):
  pass
class NameError(Exception):
  pass
class TypeError(Exception):
 pass
class Vechiles:
   def __init__(self,manufactor,model,year,type_vechile):
    self.manufactor = manufactor
    self.model = model
    self.year = year
    self.type_vechile = type_vechile
    self.start = False
    
    try:
     if type(self.year) != int:
      raise TypeError("year should be integer")
    except TypeError as te:
      print(te)
    
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
      try:
       if self.no_of_doors < 0:
        raise ValueError("No doors should be positive number")
       elif not self.type_vechile:
        raise NameError("Vechile type should not be empty")
      except ValueError as e:
       print(e)
      except NameError as ne:
       print(ne)
      
      
    def honking(self):
       print("it is honking")
      
    
class Tractors(Vechiles):

      
       def __init__(self,manufactor,model,year,type_vechile,no_of_doors,trailer_locked,fuel_levl):
         self.trailer_locked = trailer_locked
         self.fuel_levl = fuel_levl
         super().__init__(manufactor,model,year,type_vechile)
         try:
            if not self.type_vechile:
                raise NameError("Type of vehicle should not be empty")
         except NameError as ne:
            print(ne)
         except TypeError as te:
            print(te)
       def __str__(self):
          return f"{self.manufactor} {self.type_vechile}"
         
       def starting(self):
        try:
         if self.trailer_locked:
           print("Trailer is unlocked tractor is starting")
         elif self.fuel_levl > 30 and self.fuel_levl < 49:
           raise ValueError("This is a remainder Tractor fuel is below the half tank")
         elif self.fuel_levl > 49:
           raise ValueError("Tractor fuel is good")
           super().starting()
         elif self.fuel_levl < 0:
           raise ValueError("fuel level is not negative ")
        
        except ValueError as e:
          print(e)

          
     
       def stopping(self):
        try:
         if not self.trailer_locked:
           print("Trailer is locked you need to unlock to start the tractor")
         elif self.fuel_levl == 0:
          raise ValueError("Need to fill the fuel to start the tractor")
          super().stopping()
         else:
           raise ValueError("not a valid operation")
        except ValueError as e:
         print(e)

          
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
try:         
    Camry = Cars("Camry","le",2024,'',-2)
    john = Tractors("john_deer","le","2012",'',4,False,-10)

    deer = JohnDeer("john_deer","xyz",2010,'jeep',6,False,30)
    
    print(Camry)
    john.starting()
    john.stopping()
    
    john.vech_type()

    print(deer.vech_type())

except Exception as e:
  print("exception occured",e)

