class dog:
    nothing = 'This is nothing'
    count=1

    def __init__(self,name,age):
        self.name= name
        self.age = age
        count+=1
    
    def description(self):
        print(f'{self.name} is {self.age} years old')
    
    def speak(self, sound):
        return print(f'{self.name} sounds {sound}')
    
