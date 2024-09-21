import json
import re
from unidecode import unidecode

# Load the data from the json file
file_path = "cities_en.json"
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

def replace_turkish_letters(text):
    if isinstance(text, str):
        return unidecode(text).lower()
    else:
        return text

class City:
    def __init__(self, name: str, plate: str, latitude: str, longitude: str, counties: list):
        self.name = replace_turkish_letters(name)
        self.plate = plate
        self.latitude = latitude
        self.longitude = longitude
        self.counties = counties
        for county in self.counties:
            county = replace_turkish_letters(county)

    def __str__(self):
        return f"City: {self.name}, Plate: {self.plate}, Latitude: {self.latitude}, Longitude: {self.longitude}, Counties: {self.counties}"
                                                                                                                            
    def get_name(self):
        return self.name
    
    def get_plate(self):
        return self.plate
    
    def get_latitude(self):
        return self.latitude
    
    def get_longitude(self):
        return self.longitude
    
    def get_counties(self):
        return self.counties
    

class Cities:
    def __init__(self):
        self.city_list = []
    
        for city_data in data:
            name = city_data['name']
            plate = city_data['plate']
            latitude = city_data['latitude']
            longitude = city_data['longitude']
            counties = list(city_data['counties'])

            city_object = City(name,plate,latitude,longitude,counties)

            self.city_list.append(city_object)
    

    def get_city_names_list(self):
        city_names = [x.name for x in self.city_list]
        return city_names

    def get_city_by_name(self, city_name):
        city_name = replace_turkish_letters(city_name)
        for city_object in self.city_list:
            if str(city_object.name) == str(city_name):
                return city_object
        return None
    
    def search_city_name_in_text(self, text):
        text = str(replace_turkish_letters(text))
        for city_object in self.city_list:
            if city_object.name in text:
                return city_object.name
        return None

    def get_city_name_list_by_county(self, countie_name):
        possible_cities = []
        for city in self.city_list:
            if countie_name in city.counties:
                possible_cities.append(city)

        return [x.name for x in possible_cities]

    def search_counties_in_text(self, text):
        """
        Search for any full county name in the given text.
        Return: The name of the specific city if there is only one city with the county name in the text.
        """
        city_with_county = []
        text = replace_turkish_letters(text)
        for city in self.city_list:
            for county in city.counties:
                name_of_county = replace_turkish_letters(county)
                
                # Use regex to ensure full word match (surrounded by word boundaries)
                if re.search(rf'\b{name_of_county}\b', text):
                    city_with_county.append(city)
                    break  # Assuming a county should be unique within a city


        
        if len(city_with_county) == 1:
            return city_with_county[0].name
        else:
            return None

if __name__ == '__main__':
    cities = Cities()
    """
    print(cities.get_city_names_list())
    print("---------------------")
    print("Bursa:", cities.get_city_by_name("bursa"))
    print("---------------------")
    print("KemalPaşa:", cities.get_city_name_list_by_county("KEMALPAşa"))
    print("---------------------")
    #print("Search City Name in Text:", cities.search_city_name_in_text('i̇stanbul-şişli'))
    print("---------------------------------------------------------------------------------")
    """
    print("Search County in Text:", cities.get_city_name_list_by_county("cayeli"))
    # Test code to show the difference
    text = "cayeli çok güzel knk"

    print("Search County in Text:", cities.search_counties_in_text(text))

