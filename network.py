from trie import Trie
from heap import Minheap
from exceptions import InvalidHeapKvalue, NetworkLineError, NetworkStationDoesNotExistError

class Network:
    def __init__(self):
        self.lines = {}
        self.predictions = []
        self.predictions_by_station = {}
        self.stations = {}
        self.station_prefix = Trie()

    def add_line(self, line):
        self.lines[line.line_id] = line

    def get_line(self, line_id):
        if line_id not in self.lines:
            raise NetworkLineError("Line does not exist")
        return self.lines[line_id]

    def add_station(self, station):
        if station.station_id not in self.stations:
            self.stations[station.station_id] = station
            self.station_prefix.insert(station.station_name.lower(), station)

    def get_station(self, station_id):
        if station_id not in self.stations:
            raise NetworkStationDoesNotExistError("No such station in network")
        return self.stations[station_id]

    def add_prediction(self, prediction):
        self.predictions.append(prediction)
        self.predictions_by_station.setdefault(prediction.naptan_id, []).append(prediction)

    def search_by_prefix(self, prefix):
        result = []
        seen_station_ids = set()

        matches = self.station_prefix.search_by_prefix(prefix.lower())

        if prefix == "":
            return matches

        for st in matches:
            if st.station_id not in seen_station_ids:
                seen_station_ids.add(st.station_id)
                result.append(st)

        return result

    def K_preds(self, predictions, k):
        if k < -1:
            raise InvalidHeapKvalue("Cannot fetch K elements as K is invalid")

        pred_list = list(predictions)
        pred_heap = Minheap.heapify(
            [(pred.time_to_station, pred) for pred in pred_list]
        )

        result = []
        if k == -1:
            k = len(pred_heap)

        while pred_heap and len(result) < k:
            result.append(pred_heap.pop())

        return result

    def next_arrivals_by_station(self, station_id, k):
        stations = []

        for prediction in self.predictions_by_station.get(station_id, []):
            stations.append(prediction)

        return self.K_preds(stations, k)

    def next_arrivals_by_line(self, line_id, k):
        all_preds = []

        for pred in self.predictions:
            if pred.line_id == line_id:
                all_preds.append(pred)

        return self.K_preds(all_preds, k)

    def next_arrivals_by_station_and_line(self, station_id, line_id, k):
        all_preds = []

        for pred in self.predictions_by_station.get(station_id, []):
            if pred.line_id == line_id:
                all_preds.append(pred)

        return self.K_preds(all_preds, k)

    def next_stations_by_train(self, vehicle_id, line_id, k):
        all_preds = []

        for pred in self.predictions:
            if pred.vehicle_id == vehicle_id and pred.line_id == line_id:
                all_preds.append(pred)

        return self.K_preds(all_preds, k)

    def __repr__(self):
        return f"Network(no_of_lines={len(self.lines)}, no_of_stations={len(self.stations)})"
