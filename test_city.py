import unittest
from country_city import get_formatted_data


class CitiesCountryTest(unittest.TestCase):

    def test_formatted_data(self):
        data = get_formatted_data('ukraine', 'lviv')
        self.assertEqual(data, 'Ukraine, Lviv')

    def test_formatted_data_different_letters(self):
        data = get_formatted_data('uKraInE', 'lViv')
        self.assertEqual(data, 'Ukraine, Lviv')

    def test_formatted_data_population(self):
        data = get_formatted_data('uKraInE', 'lViv', 2000)
        self.assertEqual(data, 'Ukraine, Lviv population=2000')


if __name__ == '__main__':
    unittest.main()
