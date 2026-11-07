import re
import math
from exceptions import InvalidLatLonError

# Checking if Latitude and Longitude are in real-world value range
def checkLatLon(lat, lon):
        if lat < - 90 or lat > 90:
            raise InvalidLatLonError("Latitude must be between -90 and 90 degrees.")
        if lon < -180 or lon > 180:
            raise InvalidLatLonError("Longitude must be between -180 and 180 degrees.")

# Constructing a Line Modes list so that we can retain the information on modes for each line as we loose this info when we parse 
# interchange lines later we use Line Modes in is_interchange method 
def line_mode_constructor(line_modes, interchange_lines):
    for line in interchange_lines:
        line_id = line['id']
        if line_id not in line_modes:
            line_modes[line_id] = []
        for mode in line_modes[line_id]:
            if mode not in line_modes[line_id]:
                line_modes[line_id].append(mode)

class Station:
    # Initializing Class using constructor and the variables that have been provided
    def __init__(self, station_id, station_name, interchange_lines, zones, lat, lon):
        checkLatLon(lat, lon)
        self.line_modes = {}
        line_mode_constructor(self.line_modes, interchange_lines)
        self.station_id = station_id
        self.station_name = station_name
        self.interchange_lines = [line['id'] for line in interchange_lines] 
        self.zones = re.split(r'\s*[+/]\s*', zones)
        if lat < -90 and lat > 90:
            raise Exception("Latitude out of range")
        self.lat = lat

        if lon < -180 and lon > 180:
            raise Exception("Longitude out of range")
        self.lon = lon

    # Checking if this instance of station is a interchange or not by counting the number of lines that go through it
    def is_interchange(self):
        count = 0
        for line in self.line_modes:
            if "tube" in line[line['id']]:
                count += 1

        return count > 0

    # Using Haversine Formula to calculate distance between 2 stations (self and other)
    def distance_to(self, other):
        r = 6371
        dlat = math.radians(other.lat - self.lat)
        dlon = math.radians(other.lon - self.lon)
        a = math.sin(dlat/2)**2 + math.cos(math.radians(self.lat)) * math.cos(math.radians(other.lat)) * math.sin(dlon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

        return r * c

    def __eq__(self, other):
        return self.station_id == other.station_id

    def __hash__(self):
        return hash(self.station_id)

    def __repr__(self):
        return f"Station({self.station_id}, {self.station_name}, {self.interchange_lines}, {self.zones}, {self.lat}, {self.lon})"

    def __str__(self):
        return f"Station {self.station_id} {self.station_name} at ({self.lat}, {self.lon}) with zones {self.zones} and interchange lines {self.interchange_lines}"

