def get_formatted_data(country, city, population=None):
    full_data = f'{country.lower()}, {city.lower()}'
    return full_data.title() + (" population=" + str(population) if population else "")

