import unittest
import parameterized


class Person:

    def __init__(self, firstName, lastName):
        self._firstName = firstName
        self._lastName = lastName

    @property
    def FirstName(self):
        return self._firstName

    @FirstName.setter
    def FirstName(self, value):
        self._firstName = value

    @property
    def LastName(self):
        return self._lastName

    @LastName.setter
    def LastName(self, value):
        self._lastName = value

    def getFullName(self):
        return self.FirstName + self.LastName


class PersonTest(unittest.TestCase):

    # called for each test
    def setUp(self):
        pass

    @parameterized.parameterized.expand([
        ('Ryan', 'Choudhary', 'RyanChoudhary'),
        ('Gaurav', 'Choudhary', 'GauravChoudhary')
    ])
    def test_getFullName(self, firstName, lastName, expectedResult):
        person = Person(firstName, lastName)
        self.assertEqual(person.getFullName(), expectedResult)

    def test_getFirstName(self):
        person = Person('Ryan', 'Choudhary')
        self.assertEqual(person.FirstName, 'Ryan')

    def test_setFirstName(self):
        person = Person('Ryan', 'Choudhary')
        person.FirstName = 'Gaurav'
        self.assertEqual(person.FirstName, 'Gaurav')

    # called for each test
    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
