class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        self.id = name[0] + last_name + str(birth_year)


input_name = input()
input_last_name = input()
input_birth_year = input()

student = Student(input_name, input_last_name, input_birth_year)
print(student.id)
