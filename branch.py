class Branch:
    # Initializing the constructor with given variables and also initializing a stations list 
    def __init__(self, branch_id, next_branch_ids):
        self.branch_id = branch_id
        self.next_branch_ids = next_branch_ids
        self.stations = []

    # Adding the station to stations list
    def add_station(self, station):
        self.stations.append(station)

    # Creating a st_edges list to store all the edges between stations by traversing stations list
    def station_edges(self):
        st_edges = []
        for i in range(len(self.stations) - 1):
            st_edges.append((self.stations[i], self.stations[i + 1]))

        return st_edges

    # Creating a br_edges list to store all the edges between stations by traversing stations list
    def branch_edges(self):
        br_edges = []
        for next_id in self.next_branch_ids:
            br_edges.append((self.branch_id, next_id))

        return br_edges

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

        
