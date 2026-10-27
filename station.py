import re
import math
# Split the zones string on either '+' or '/', handling both delimiters, into a list of zones,
# and parse interchange_lines (a list of line records, each carrying an id) into a list of
# line ids. Add checks that lat and lon fall within valid real-world latitude and longitude
# ranges, otherwise throw an exception;
def checkLatLon(lat, lon):
        if lat < - 90 or lat > 90:
            raise ValueError("Latitude must be between -90 and 90 degrees.")
        if lon < -180 or lon > 180:
            raise ValueError("Longitude must be between -180 and 180 degrees.")

def line_mode_constructor(line_modes, interchange_lines):
    for line in interchange_lines:
        line_id = line['id']
        if line_id not in line_modes:
            line_modes[line_id] = []
        for mode in line['modes']:
            if mode not in line_modes[line_id]:
                line_modes[line_id].append(mode)

class Station:
    line_modes = {}
    def __init__(self, station_id, station_name, interchange_lines, zones, lat, lon):
        checkLatLon(lat, lon)
        line_mode_constructor(self.line_modes, interchange_lines)
        self.station_id = station_id
        self.station_name = station_name
        self.interchange_lines = [line['id'] for line in interchange_lines]
        self.zones = re.split(r'\s*[+/]\s*', zones)
        self.lat = lat
        self.lon = lon


    def is_interchange(self):
        count = 0
        for line in self.line_modes:
            if "tube" in line[line['id']]:
                count += 1

        return count > 0

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