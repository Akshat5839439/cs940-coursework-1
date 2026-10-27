class Prediction:
    def __init__(self, vehicle_id, naptan_id, line_id, platform_name, destination_id, time_to_station, current_location):
        self.vehicle_id = vehicle_id
        self.naptan_id = naptan_id
        self.line_id = line_id
        self.platform_name = platform_name
        self.destination_id = destination_id
        self.time_to_station = lambda x: time_to_station if time_to_station >= 0 else Exception("Time to Station is less than 0")
        self.current_location = current_location

    def __lt__(self, other):
        v_id1 = int(self.vehicle_id)
        v_id2 = int(other.vehicle_id)

        return (self.time_to_station, self.vehicle_id) < (other.time_to_station, other.vehicle_id)

    def __repr__(self):
        return f"Prediction(vehicle_id={self.vehicle_id}, naptan_id={self.naptan_id}, line_id={self.line_id}, platform_name={self.platform_name}, destination_id={self.destination_id}, time_to_station={self.time_to_station}, current_location={self.current_location})"