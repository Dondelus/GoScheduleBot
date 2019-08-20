from datetime import datetime
from datetime import time

from reader import DbReader


class Route:
    def __init__(
        self,
        id,
        short_name,
        origin,
        destination,
        long_name =None,
        schedule=None,
        first_departure=None,
        last_departure=None
    ):
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

    def get_cost(self, origin, destination):
        ''' Return the Presto cost (in CAD) of traveling from origin to destination on this route. '''
        try:
            return self.stops[destination] - self.stops[origin] # load in prices.txt later to calculate
        except:
            raise ValueError('Origin or destination is invalid.')