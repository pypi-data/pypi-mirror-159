import requests


class Weather:
    """Creates a Weather object getting an apikey as input and either a city name or lat and lon coordiantes.

    Package usage example:

    # Create a weather object using a city name:
    # The api key below will probably not work.
    # Get your own apikey on https://openweathermap.org
    # Wait till it is activated

    >>> weather1 = Weather(city="Budapest", apikey="99c31e51955e20bc1340417d85574569")

    # Using latitude and longtitude coords
    >>> weather2 = Weather(lat=41.4858, lon=72.0396, apikey="99c31e51955e20bc1340417d85574569")

    # Get full weather data for the next 12 hours:
    >>> weather1.next_12h()

    # Simplified data for the next 12 hours:
    >>> weather1.next_12h_simplified()

    Sample url to get sky condition icons:
    http://openweathermap.org/img/wn/10d@2x.png

    """

    def __init__(self, apikey, city=None, lat=None, lon=None):

        if city:
            r = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?q={city}'
                             f'&APPID={apikey}'
                             f'&units=metric')
            self.data = r.json()
        elif lat and lon:
            r = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}'
                             f'&APPID={apikey}'
                             f'&units=metric')
            self.data = r.json()
        else:
            raise TypeError("Provide either a city or lat/lon arguments")

        if self.data['cod'] != '200':
            raise ValueError(self.data['message'])

    def next_12h(self):
        """Returns 3-hour data for the next 12 hours as a dictionary
        """
        return self.data['list'][:4]  # get four items of list i.e. 12 hours of data

    def next_12h_simplified(self):
        """Returns date, temp and sky condition every 3 hours for the next 12 hours as a list of tuples
        """
        weather_list = []
        for weather in self.data['list'][:4]:
            weather_list.append((weather['dt_txt'],
                                 weather['main']['temp'],
                                 weather['weather'][0]['description'],
                                 weather['weather'][0]['icon']))
        return weather_list
