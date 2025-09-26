import pickle
import datetime

class Cat:

    def __init__(self, name, race):
        self.name = name
        self.race = race
        self.datetime_of_birth = datetime.datetime.now()
    
    def __str__(self):
        return f"{self.name} is a {self.race}"

    def __eq__(self, value) -> bool:
        if isinstance(value, Cat):
            return self.name == value.name and self.race == value.race  
        return False
        

    def __hash__(self) -> int:
        hash_Value= hash((self.name,self.race))

        return hash_Value
    
    #*Save
    def __getstate__(self):
        state = self.__dict__.copy()
        #Do stuff here
        state['name'] = "Obelix but loaded"
        return state
    
    #*Load
    def __setstate__(self, state):
        state['race'] = "Loaded cat race"
        self.__dict__.update(state)
        
    
        
    def meow(self) -> tuple[str,str]:
        return self.name, "says Meow!"




obelix = Cat("Obelix", "European Shorthair")

with open("cats.cat", "wb") as f:
    pickle.dump(obelix, f)

with open("cats.cat", "rb") as f:
    loaded_cat: Cat = pickle.load(f)

print("Object: ",obelix)
print("Loaded: ",loaded_cat)

