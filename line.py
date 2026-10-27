from branch import Branch
class Line:
    branches = {}
    def __init__(self, line_id, line_name):
        self.line_id = line_id
        self.line_name = line_name

    def add_branch(self, branch):
        self.branches[self.line_id] = branch

    def get_branch(self, id):
        return self.branches[id]

    def get_stations(self):
        all_station_ids = set()
        for branch in self.branches.values():
            for station_id in branch.stations:
                all_station_ids.add(station_id)
        return all_station_ids
    
    
    def __iter__(self):
        return iter(self.branches)

    def __len__(self):
        return len(self.branches)


    def __contains__(self, item):
        return item in self.branches

    def __repr__(self):
        return f"Line(line_id={self.line_id}, line_name={self.line_name}, branches={self.branches})"