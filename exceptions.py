# Tube Related Exceptions
class TubeError(Exception):
    pass


class InvalidLatLonError(TubeError):
    pass


class InvalidBranchIdError(TubeError):
    pass


class InvalidTimeToStationError(TubeError):
    pass


# Data Structure Related Errors
class DataStructureError(TubeError):
    pass


class HeapError(DataStructureError):
    pass


class HeapEmptyError(HeapError):
    pass


class InvalidHeapKvalue(HeapError):
    pass


class NetworkLineError(DataStructureError):
    pass


class NetworkStationDoesNotExistError(DataStructureError):
    pass