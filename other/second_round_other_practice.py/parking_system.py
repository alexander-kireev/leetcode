class ParkingSystem():
    def __init__(self, big, medium, small):
        self.spaces = {
            1: {
                "capacity": big,
                "taken": 0
            },
            2: {
                "capacity": medium,
                "taken": 0
            },
            3: {
                "capacity": small,
                "taken": 0
            }

        }

    def add_car(self, car_type):
        if self.spaces[car_type]["taken"] < self.spaces[car_type]["capacity"]:
            self.spaces[car_type]["taken"] += 1
            return True
        return False
    