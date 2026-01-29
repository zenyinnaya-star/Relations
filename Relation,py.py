class Person:
    def __init__(self, fname, age, lname,favorite_color,person_id,is_working):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.favorite_color=favorite_color
        self.person_id=person_id
        self.is_working=is_working
    def display(self):
        print(f'personal id : {self.person_id}\nname: {self.fname} {self.lname}\nfavorite color: {self.favorite_color}\nage: {self.age}\nworking status: {self.is_working}')
    def changeFavoriteColour (self,new_color):
        self.favorite_color=new_color
        print(f'new favorite color is {self.favorite_color}')
    def getAgeInTenYears (self):
        return self.age + 10
    def displaysample(self):
        print(f"{self.fname} is favorite color is {self.favorite_color}\npersonal id : {self.person_id}")   
    
    def __str__(self):
        return f'person[id={self.person_id}, name={self.fname} {self.lname}, age={self.age}]'


class Relation:
    """Class to represent relationships between Person objects"""
    
    def __init__(self, relationshipType):
        """
        Initialize Relation with a relationship type
        
        Args:
            relationshipType: Must be one of 'Sister', 'Brother', 'Mother', or 'Father'
        """
        valid_types = ['Sister', 'Brother', 'Mother', 'Father']
        
        if relationshipType not in valid_types:
            raise ValueError(f"Invalid relationship type. Must be one of {valid_types}")
        
        self.relationshipType = relationshipType
    
    def showRelationShip(self, person1, person2):
        """
        Display the relationship between two Person objects
        
        Args:
            person1: First Person object
            person2: Second Person object
        """
        if not isinstance(person1, Person) or not isinstance(person2, Person):
            print("Error: Both parameters must be Person objects")
            return
        
        print(f"Relationship: {person1.fname} {person1.lname} is the {self.relationshipType} of {person2.fname} {person2.lname}")
class Main:
    def __init__(self):
        self.p1=Person("ian",30,"Brooks","Red",1,True)
        self.p2=Person("Gina",18,"James","Green",2,False)
        self.p3=Person("Mike",45,"Brisco","Blue",3,True)
        self.p4=Person("Mary",28,"Beals","Yellow",4,True)
        self.people = [self.p1, self.p2, self.p3, self.p4]
        print("="*80)
        self.averageAge()
        print("="*80)
        self.youngestPerson()
        print("="*80)
        self.oldestPerson()
        print("="*80)
        self.firstnamewithM()
        print("="*80)
        self.favouriteblue()
        
    
    def averageAge(self):
        total_age = sum(person.age for person in self.people)
        average_age = total_age / len(self.people)
        print(f"The average age is: {average_age}")
    
    def youngestPerson(self):
        youngest = min(self.people, key=lambda person: person.age)
        print(f"The youngest person is: {youngest.fname} {youngest.lname}, Age: {youngest.age}")
    
    def oldestPerson(self):
        oldest = max(self.people, key=lambda person: person.age)
        print(f"The oldest person is: {oldest.fname} {oldest.lname}, Age: {oldest.age}")
    
    def firstnamewithM(self):
        m_names = [person.fname for person in self.people if person.fname.startswith('M')]
        print("First names starting with 'M':", ', '.join(m_names))
    
    def favouriteblue(self):
        blue_fans = [person.fname for person in self.people if person.favorite_color.lower() == 'blue']
        print("People whose favorite color is blue:", ', '.join(blue_fans))
        
        print("="*80)
        self.p3.display()
        print("="*80)
        self.p1.changeFavoriteColour("White") 
        print("="*80) 
        self.p1.displaysample()
        print("="*80)
        
        relation1 = Relation("Brother")
        relation1.showRelationShip(self.p1, self.p3)
        
        print("="*80)
        relation2 = Relation("Sister")
        relation2.showRelationShip(self.p2, self.p4)
        print("="*80)
        
    
    
    
    


if __name__ == "__main__":
    Main()
 
    