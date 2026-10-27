class Branch:
    stations = []

    def __init__(self, branch_id, next_branch_ids):
        self.branch_id = branch_id
        self.next_branch_ids = next_branch_ids
    
    def add_station(self, station):
        self.stations.append(station)

    def station_edges(self):
        edges = []
        for i in range(len(self.stations) - 1):
            edges.append((self.stations[i], self.stations[i + 1]))

        return edges

    def branch_edges(self):
        edges = []
        for next_id in self.next_branch_ids:
            edges.append((self.branch_id, next_id))

        return edges

    def __iter__(self):
        return iter(self.stations)

    def __len__(self):
        return len(self.stations)

    def __contains__(self, station):
        return station in self.stations

    def __getitem__(self, index):
        return self.stations[index]

    def __repr__(self):
        return f"Branch(branch_id={self.branch_id}, next_branch_ids={self.next_branch_ids}, stations={self.stations})"

        
