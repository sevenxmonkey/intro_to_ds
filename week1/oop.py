class Person:
    department = 'Software Development'

    def set_name(self, new_name):
        self.name = new_name
    def set_location(self, new_location):
        self.location = new_location

personA = Person()
personA.set_name('Xiaowen Xu')
personA.set_location('Santa Clara, CA, USA')

print('{} live in {} and works in the department {}'.format(personA.name, personA.location, personA.department))