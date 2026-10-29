# Define a base class TubeError(Exception) in exceptions.py, from which all Tube-
# related custom exceptions you write will inherit.
class TubeError(Exception):
    def __init__(self, message):
        self.message = ""
        super().__init__(self.message)

    def valueError(self):
        return




# Define a base class DataStructureError(Exception) in exceptions.py, from which all
# data structure-related custom exceptions you write will inherit.
class DataStructureError(Exception):
    def __init__(self, message):
        self.message = "base Error class DataStructureError"
        super().__init__(self.message)