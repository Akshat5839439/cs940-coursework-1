from trie import Trie
from line import Line
from prediction import Prediction
from station import Station

class Network:
    def __init__(self):
        self.network = {
            "line": {},
            "station": {},
            "prediction": {}
        }
        self.station_prefix = Trie()

    def add_line(self, line):
        self.network["line"][line.line_id] = line.line_name

    def get_line(self, line_id):
        if line_id not in self.network["line"]:
            raise Exception("Line does not exist")
        return self.network["line"][line_id]

    def add_station(self, station):
        s_name = station.station_name.lower()
        self.network["station"][station.station_id] = s_name
        self.station_prefix.insert(s_name, station)

    def get_station(self, station_id):
        if station_id not in self.network["station"]:
            raise Exception("No such station in network")
        return self.network[station_id]

    def add_prediction(self, prediction):
        train_key = f'{prediction.vehicle_id}{prediction.line_id}'
        self.network["prediction"][train_key] = prediction

    def search_by_prefix(self, prefix):
        return self.station_prefix.search_by_prefix(prefix).station_name

    def next_arrivals_by_station(self, station_id, k):
        result = []

        for pred in self.network["prediction"]:
            if len(result) == k:
                break
            if pred.naptan_id == station_id:
                result.append(pred)

        return result

    def next_arrivals_by_line(self, line_id, k):
        result = []

        for pred in self.network["prediction"]:
            if len(result) == k:
                break

            if pred.line_id == line_id:
                result.append(pred)

        return result

    def next_arrivals_by_station_line(self, station_id, line_id, k):
        result =[]

        for pred in self.network["prediction"]:
            if len(result) == k:
                break

            if pred.line_id == line_id and pred.naptan_id == station_id:
                result.append(pred)

        return result

    def next_stations_by_train(self, vehicle_id, line_id, k):
        result = []

        for pred in self.network["prediction"]:
            if len(result)  == k:
                break

            if pred.line_id == line_id and pred.vehicle_id == vehicle_id:
                result.append(pred)

        return result

    def __repr__(self):
        return f"Network(no_of_lines={len(self.network["line"])}, no_of_stations={len(self.network["station"])})"