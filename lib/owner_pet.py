class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    def __init__(self, name, pet_type, owner=""):
        
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Must be pet from PET_TYPES list.")
            
        else:
            self.pet_add(self)
        
    @classmethod
    def pet_add(cls, pet):
        cls.all.append(pet)

class Owner:
    def __init__(self, name):
        self.name = name
    def pets(self):
        print([pet for pet in Pet.all if self.name == pet.owner.name])
        return [pet for pet in Pet.all if self.name == pet.owner.name]

    def add_pet(self, pet):
        self.pet = pet
        if not isinstance(pet, Pet):
            raise Exception("Must be pet from PET_TYPES list.")
            
        else:
            pet.owner = self
    def get_sorted_pets(self):
        # print(self.name.sort())
        # print(sorted(self.pets(), key=lambda pet: pet.name))
        return sorted(self.pets(), key=lambda pet: pet.name)
                
        
        


# bird = Pet("Polly", "bird")
# print(bird.owner)
# owner = Owner("John")
# pet1 = Pet("Fido", "dog", owner)
# pet2 = Pet("Clifford", "dog", owner)
# pet3 = Pet("Whiskers", "cat", owner)
# pet4 = Pet("Jerry", "reptile", owner)
# owner.get_sorted_pets()
