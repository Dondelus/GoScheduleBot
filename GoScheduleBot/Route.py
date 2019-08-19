from datetime import datetime
from datetime import time

class Route:
    def __init__(self, id:str, short_name:str, origin:str, destination:str, long_name:str =None, schedule:list=None, first_departure:datetime=None, last_departure:datetime=None) -> Route:
        self.id = id
        self.short_name = short_name
        self.long_name = long_name
        self.origin = origin
        self.destination = destination
        self.stops = None
        self.schedule = schedule
        self.first_departure = first_departure
        self.last_departure = last_departure


    def set_stops(self) -> None:
        '''
        Set a route's stops to a dictionary with (key, value) of stop_name (str), cost_from_origin (long).
        The price of stops[origin] is always 0.0.
        '''
        self.stops = {}

    def get_cost(self, origin:str, destination:str) -> long:
        ''' Return the Presto cost (in CAD) of traveling from origin to destination on this route. '''
        try:
            price = self.stops[destination] - self.stops[origin]
            return max(price, 3.70)
        except:
            raise ValueError('Origin or destination is invalid.')