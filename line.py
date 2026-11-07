from branch import Branch
from exceptions import InvalidBranchIdError

class Line:
    # Initializing the constructor with the variables given in the task and initialziing a dictionary called branches
    def __init__(self, line_id, line_name):
        self.line_id = line_id
        self.line_name = line_name
        self.branches = {}

    # Storing branch details with branch id as key in branches dictionary
    def add_branch(self, branch):
        self.branches[branch.branch_id] = branch

    # Retrieving branch using the id provided from the branches dictionary
    def get_branch(self, branch_id):
        if branch_id not in self.branches:
            raise InvalidBranchIdError(f"No branch with ID: {branch_id} found")
        return self.branches[branch_id]

    # Retrieving all station IDs from the Branches dictionary
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