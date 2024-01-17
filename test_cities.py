import unittest
from country_cities import get_formatted_data


class CitiesCountryTest(unittest.TestCase):

    def test_formatted_data(self):
        data = get_formatted_data('ukraine', 'lviv')
        self.assertEqual(data, 'Ukraine, Lviv')


if __name__ == '__main__':
    unittest.main()