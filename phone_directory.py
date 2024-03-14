class phone_directory(object):
    all_names = []
    def __init__(self,name,age,address,phone,occupation):
     self.name = name
     self.age = age
     self.address = address
     self.phone = phone
     self.occupation = occupation
     phone_directory.all_names.append(self)
    
   
    def __str__(self):
       return str(self.phone) + ' ' + self.name
       
    def find_name(name):
        return filter(lambda obj: obj.name == name, phone_directory.all_names)
    def find_age(age):
        return filter(lambda obj: obj.age == age, phone_directory.all_names)
        
      
    
        
uday = phone_directory("Uday", 24, "3200 west chappel rd  ", 4567890341,"student")
shyam = phone_directory("shyam", 25, "3200 west university dr   ", 4675678902,"professor")

print(uday)
print(shyam)

print([obj.name for obj in phone_directory.all_names])
print([obj.name for obj in phone_directory.find_name("Uday")])
print ([obj.name for obj in phone_directory.find_age(25)])
