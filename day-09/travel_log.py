travel_log = [
        {
            'country': 'France',
            'visits': 12,
            'cities': ['Paris', 'Lille', 'Dijon']
        },
        {
            'country': 'Germany',
            'visits': 5,
            'cities': ['Berlin', 'Hamburg', 'Stuttgart']
        },
    ]

def add_new_country(country:str, visited:int, cities:list[str]):
        
    country_dict = {}
    country_dict['country'] = country
    country_dict['visits'] = visited
    country_dict['cities'] = cities
    travel_log.append(country_dict)

if __name__ == '__main__':

    add_new_country('Russia', 2, ['Moscow','Saint Petersberg'])
    print(travel_log)