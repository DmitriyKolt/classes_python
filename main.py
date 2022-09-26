class People():
    people_col=0
    def __init__(self, name, surname, sex, age, prof):
        self.name = name
        self.surname = surname
        self.sex = sex
        self.age = age
        People.people_col += 1


    def people_info(self):
        print(People.people_col, self.name, self.surname, self.sex, self.age)

people1 = People('Dmitriy', 'Koltakov', 'man', '15')
people1.people_info()


