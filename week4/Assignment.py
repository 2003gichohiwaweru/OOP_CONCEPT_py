class person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
       
         print(f"Hello, there My name is {self.name}. I am a {self.gender} {self.age} years old. ")


def get_gender_input():
    gender_options = ['male', 'female', 'other']
    while True:
        gender = input("Enter your gender (male/female/other): ").lower()
        if gender in gender_options:
            return gender
        else:
            print("Invalid input. Please enter either 'male', 'female', or 'other'.")
     

name = input("Enter Your name: ")
age = int(input("Enter you age in numbers : "))
gender = get_gender_input()

person1 = person(name, age, gender)

person1.introduce()

